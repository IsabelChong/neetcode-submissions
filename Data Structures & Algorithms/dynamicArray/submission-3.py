class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.cap = capacity

    def get(self, i: int) -> int:
        if i > self.cap: 
            return None
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i > self.cap: 
            return None
        self.arr[i] = n
        return None

    def pushback(self, n: int) -> None:
        if len(self.arr) == self.cap:
            self.resize()
        self.arr.append(n)
        return None

    def popback(self) -> int:
        return self.arr.pop()

    def resize(self) -> None:
        self.cap *= 2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.cap