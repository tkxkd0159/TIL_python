from . import PI

class Circle:
    """[summary]
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return PI * self.radius ** 2
