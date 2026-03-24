from utils import argument_error, parse_int


class Commands:
    def execute(self, command, args, context):
        name = command.upper()

        if name == "ADD_PLAYER":
            self.add_player(args, context)
            return True
        if name == "UPDATE_SCORE" or name == "ADD_SCORE":
            self.update_score(args, context)
            return True
        if name == "REMOVE_PLAYER":
            self.remove_player(args, context)
            return True
        if name == "LIST_PLAYERS" or name == "PRINT_ALL":
            self.list_players(args, context)
            return True
        if name == "SCORE_HISTORY":
            self.score_history(args, context)
            return True
        if name == "HISTORY":
            self.history(args, context)
            return True
        if name == "CURRENT":
            self.current(args, context)
            return True
        if name == "BEST":
            self.best(args, context)
            return True
        if name == "TOP_K":
            self.top_k(args, context)
            return True
        if name == "CLEAR":
            self.clear(args, context)
            return True
        if name == "LEN":
            self.length(args, context)
            return True
        if name == "QUIT":
            self.quit(args, context)
            return False

        raise ValueError(f"Unknown command '{command}'")

    def add_player(self, args, context):
        argument_error("ADD_PLAYER", args, 1)
        context.service.add_player(args[0])

    def update_score(self, args, context):
        argument_error("UPDATE_SCORE", args, 2)
        score = parse_int(args[1], "score")
        context.service.update_score(args[0], score)

    def remove_player(self, args, context):
        argument_error("REMOVE_PLAYER", args, 1)
        context.service.remove_player(args[0])

    def list_players(self, args, context):
        argument_error("LIST_PLAYERS", args, 0)
        context.write_many(context.service.list_players_lines())

    def score_history(self, args, context):
        argument_error("SCORE_HISTORY", args, 1)
        context.write_many(context.service.score_history_lines(args[0]))

    def history(self, args, context):
        argument_error("HISTORY", args, 2)
        limit = parse_int(args[1], "limit")
        context.write_many(context.service.score_history_limited_lines(args[0], limit))

    def current(self, args, context):
        argument_error("CURRENT", args, 1)
        context.write(context.service.current_score(args[0]))

    def best(self, args, context):
        argument_error("BEST", args, 1)
        context.write(context.service.best_score(args[0]))

    def top_k(self, args, context):
        argument_error("TOP_K", args, 1)
        k = parse_int(args[0], "k")
        if k < 0:
            raise ValueError("k must be >= 0")
        context.write_many(context.service.top_k_lines(k))

    def clear(self, args, context):
        argument_error("CLEAR", args, 0)
        context.service.clear()

    def length(self, args, context):
        argument_error("LEN", args, 0)
        context.write(len(context.service.players))

    def quit(self, args, context):
        argument_error("QUIT", args, 0)
