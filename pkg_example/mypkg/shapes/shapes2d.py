from . import PI

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2
