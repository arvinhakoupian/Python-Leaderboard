class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def clear(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values
