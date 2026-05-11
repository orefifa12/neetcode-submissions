class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.hashTable = [[]for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket = self.hashVal(key)

        if key in self.hashTable[bucket]:
            pass
        elif self.hashTable[bucket] != []:
            self.hashTable[bucket].append(key) #LinkedChain Collision Fix
        else:
            self.hashTable[bucket] = [key] # put in bin
        
    def remove(self, key: int) -> None:
        bucket = self.hashVal(key)
        if key in self.hashTable[bucket]:
            self.hashTable[bucket].remove(key)
        else:
            pass

    def contains(self, key: int) -> bool:
        bucket = self.hashVal(key)

        for number in self.hashTable[bucket]:
            if key == number:
                return True
        
        return False

    def hashVal(self, val: int): #Hashfunction
        return val % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)