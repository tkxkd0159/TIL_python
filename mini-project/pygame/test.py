from typing import List, Type

class Test:
    def __init__(self, sample, speed=0):
        self.sample = sample
        self.speed = speed


def change_const(new: Type[Test], list_ex: List) -> List:

    global A
    NEW.sample = 100
    new.speed = 77
    list_ex = [2, 2, 2]

    A = 4
    return list_ex

if __name__ == "__main__":
    NEW = Test(32, 23)
    A = 2
    LIST = [1, 2, 3]
    print(NEW.sample)
    print(NEW.speed)
    NEW_LIST = change_const(NEW, LIST)
    print(NEW_LIST)
    print(NEW.sample)
    print(NEW.speed)
    print(A)
