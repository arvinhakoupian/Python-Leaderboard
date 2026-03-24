class DynamicArray:
    def __init__(self, initial_capacity=4):
        self.capacity = max(1, initial_capacity)
        self.size = 0
        self._data = [None] * self.capacity

    def append(self, value):
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
        self._data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        index = 0
        while index < self.size:
            new_data[index] = self._data[index]
            index += 1
        self._data = new_data
        self.capacity = new_capacity

    def to_list(self):
        output = []
        index = 0
        while index < self.size:
            output.append(self._data[index])
            index += 1
        return output
