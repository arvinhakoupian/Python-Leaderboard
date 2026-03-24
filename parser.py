class CommandParser:
    def parse(self, raw_line):
        tokens = []
        current = []
        in_quotes = False
        index = 0
        length = len(raw_line)

        while index < length:
            char = raw_line[index]

            if char == '"':
                in_quotes = not in_quotes
                index += 1
                continue

            if char.isspace() and not in_quotes:
                if len(current) > 0:
                    tokens.append("".join(current))
                    current = []
                index += 1
                continue

            current.append(char)
            index += 1

        if in_quotes:
            raise ValueError("Unclosed quote in command")

        if len(current) > 0:
            tokens.append("".join(current))

        return tokens
