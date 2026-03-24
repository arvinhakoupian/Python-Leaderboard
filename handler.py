import os

from context import CommandContext
from parser import CommandParser
from commands import Commands
from service import LeaderboardService


class Handler:
    def __init__(self, writer):
        self.writer = writer

    def run(self, argv):
        if len(argv) != 2:
            self.writer("Usage: python main.py <command_file>")
            return 1

        command_file = argv[1]
        if not os.path.isfile(command_file):
            self.writer(f"Error: cannot open file '{command_file}'")
            return 1

        parser = CommandParser()
        registry = Commands()
        service = LeaderboardService()
        context = CommandContext(service=service, writer=self.writer)

        with open(command_file, "r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                stripped = raw_line.strip()
                if stripped == "" or stripped.startswith("#"):
                    continue

                try:
                    tokens = parser.parse(stripped)
                    if len(tokens) == 0:
                        continue

                    command = tokens[0]
                    args = tokens[1:]
                    should_continue = registry.execute(command, args, context)
                    if not should_continue:
                        break
                except Exception as exc:
                    self.writer(f"ERROR: line {line_number}: {exc}")

        return 0
