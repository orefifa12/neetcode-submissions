class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        if self.capacity > 0:
            self.Array = [None] * self.capacity

    def get(self, i: int) -> int: #Done
        return self.Array[i] #O(1)

    def set(self, i: int, n: int) -> None: #Done
        self.Array[i] = n

    def pushback(self, n: int) -> None: #Done
        if self.length == self.capacity:
            self.resize()

        self.Array[self.length] = n
        self.length += 1

    def popback(self) -> int: #Done
        poppedVal = self.Array[self.length-1]
        
        self.length -= 1
        return poppedVal

    def resize(self) -> None: #Done
        oldArray = self.Array
        self.capacity *= 2
        self.Array = [None] * self.capacity
        for i in range(len(oldArray)):
            self.Array[i] = oldArray[i]

    def getSize(self) -> int: #Done
        return self.length
        
    def getCapacity(self) -> int: #Done
        return self.capacity
