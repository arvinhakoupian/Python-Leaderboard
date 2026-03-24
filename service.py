from dynamic_array import DynamicArray
from heap_sort import heap_sort
from linkedlist import LinkedList
from players import Player, PlayerList


class LeaderboardService:
    def __init__(self):
        self.players = PlayerList()

    def add_player(self, name):
        existing = self.players.find(name)
        if existing is not None:
            raise ValueError(f"Player '{name}' already exists")
        self.players.add(Player(name=name, history=LinkedList(), best=0))

    def update_score(self, name, score):
        player = self.players.find(name)
        if player is None:
            raise ValueError(f"Player '{name}' not found")

        player.history.add_first(score)
        if len(player.history) == 1 or score > player.best:
            player.best = score

    def remove_player(self, name):
        removed = self.players.remove(name)
        if not removed:
            raise ValueError(f"Player '{name}' not found")

    def clear(self):
        self.players.clear()

    def list_players_lines(self):
        if len(self.players) == 0:
            return ["EMPTY"]

        lines = []
        for player in self.players.iter_players():
            current_score = player.history.head.value if player.history.head is not None else 0
            lines.append(f"-> {player.name} | current={current_score} | best={player.best}")
        return lines

    def score_history_lines(self, name):
        player = self.players.find(name)
        if player is None:
            raise ValueError(f"Player '{name}' not found")

        values = player.history.to_list()
        if len(values) == 0:
            return ["EMPTY"]

        return [str(value) for value in values]

    def score_history_limited_lines(self, name, limit):
        if limit < 0:
            raise ValueError("limit must be >= 0")

        lines = self.score_history_lines(name)
        if lines == ["EMPTY"]:
            return lines
        return lines[:limit]

    def current_score(self, name):
        player = self.players.find(name)
        if player is None:
            raise ValueError(f"Player '{name}' not found")
        if player.history.head is None:
            return 0
        return player.history.head.value

    def best_score(self, name):
        player = self.players.find(name)
        if player is None:
            raise ValueError(f"Player '{name}' not found")
        return player.best

    def top_k_lines(self, k):
        if len(self.players) == 0:
            return ["EMPTY"]

        snapshots = DynamicArray()
        for player in self.players.iter_players():
            current_score = player.history.head.value if player.history.head is not None else 0
            snapshots.append((player.name, current_score, player.best))

        entries = snapshots.to_list()

        def compare(a, b):
            if a[2] != b[2]:
                return 1 if a[2] > b[2] else -1
            if a[1] != b[1]:
                return 1 if a[1] > b[1] else -1
            if a[0] < b[0]:
                return 1
            if a[0] > b[0]:
                return -1
            return 0

        heap_sort(entries, compare)
        entries.reverse()

        limit = k if k < len(entries) else len(entries)
        lines = []
        index = 0
        while index < limit:
            name, current_score, best_score = entries[index]
            lines.append(f"{index + 1}. {name} | current={current_score} | best={best_score}")
            index += 1

        if len(lines) == 0:
            return ["EMPTY"]

        return lines
