class CommandContext:
    def __init__(self, service, writer):
        self.service = service
        self.writer = writer

    def write(self, message):
        self.writer(str(message))

    def write_many(self, messages):
        for message in messages:
            self.writer(str(message))
