class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._i = 0

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i == 0:
            self._i += 1
            return {"length": self.length}
        elif self._i == 1:
            self._i += 1
            return {"width": self.width}
        else:
            raise StopIteration
