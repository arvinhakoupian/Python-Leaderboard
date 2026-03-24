from dataclasses import dataclass

from linkedlist import LinkedList


@dataclass
class Player:
    name: str
    history: LinkedList
    best: int


class PlayerNode:
    def __init__(self, player):
        self.player = player
        self.next = None


class PlayerList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, player):
        node = PlayerNode(player)
        node.next = self.head
        self.head = node
        self.length += 1

    def find(self, name):
        current = self.head
        while current is not None:
            if current.player.name == name:
                return current.player
            current = current.next
        return None

    def remove(self, name):
        previous = None
        current = self.head
        while current is not None:
            if current.player.name == name:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.length -= 1
                return True
            previous = current
            current = current.next
        return False

    def clear(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def iter_players(self):
        current = self.head
        while current is not None:
            yield current.player
            current = current.next
