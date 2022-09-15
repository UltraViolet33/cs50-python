class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"🍪" * self.size

    @classmethod
    def get(cls):
        cap = int(input("Capacity: "))
        return cls(cap)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer")

        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n < 0:
            raise ValueError
        self._size = n

    def deposit(self, n):
        new_total_cookies = self.size + n
        if new_total_cookies > self.capacity:
            raise ValueError("Too many cookies")

        self._size = new_total_cookies

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        new_total_cookies = self.size - n
        self._size = new_total_cookies
