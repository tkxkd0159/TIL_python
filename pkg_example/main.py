if __name__ == "__main__":

    import os
    import sys
    import mypkg
    import pathlib

    print(mypkg.cube(3))
    print(mypkg.Circle(3).area())
    print(mypkg.stats.data_range([2,3,4]))
    print(mypkg.Circle(3).__module__)
    print(mypkg.stats.data_range.__module__)

    print(f"Current Working Directory : {os.getcwd()}")
    sys.path.append(os.getcwd())
    print(pathlib.Path.cwd())
    print(pathlib.Path(__file__))
    print(pathlib.PurePath(__file__).parent)
    print(__file__)

    class MyClass():
        def __init__(self):
            self.value1 = 1
            self.value2 = 2

        def __repr__(self):
            return repr([self.value1, self.value2])

    print(MyClass())