
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be positive")
        
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies:(")
        self._size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies!(⚆ᗝ⚆)")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jart = Jar()
jart.deposit(6)

print(jart.size)