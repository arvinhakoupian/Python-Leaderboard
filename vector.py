class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:

        return self.arr[i]

    def insert(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
       if self.size == self.capacity:
            self.resize()
       
       self.arr[self.size] = n
       self.size += 1
    
    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Array is empty")

        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

da = DynamicArray(2)

da.pushback(10)
da.pushback(20)

print(da.get(0))
print(da.get(1))

da.pushback(30)

print(da.getSize())
print(da.getCapacity())

print(da.popback())
print(da.getSize())