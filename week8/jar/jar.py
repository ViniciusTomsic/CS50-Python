class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int):
            raise ValueError
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return self.cookies*'🍪'

    def deposit(self, n):
        if n + self.cookies > self._capacity:
            raise ValueError
        else:
            self.cookies += n

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError
        else:
            self.cookies += -n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

