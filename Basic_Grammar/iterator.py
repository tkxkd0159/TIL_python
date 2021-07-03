# 값을 차례대로 꺼낼 수 있는 object
# 값이 필요한 시점이 되었을 때 값을 만드는 방식 -> 숫자를 한번에 만들어 메모리에 올려서 뽑아쓰는 방식보다 메모리 아낄 수 있음
# list, tuple, str, dict, set, range

import random

def iter_example1():
    it1 = [1, 2, 3].__iter__()
    it2 = "Hello".__iter__()
    it3 = {'a': 1, 'b': 2}.__iter__()
    it4 = {7, 8, 9}.__iter__()
    it5 = iter(lambda : random.randint(0, 5), 2)

    print("==== it1 start ====")
    while True:
        try:
            print(next(it1))
        except:
            break
    print("==== it1 finish ====")

    print("==== it2 start ====")
    while True:
        try:
            print(it2.__next__())
        except:
            break
    print("==== it2 finish ====")

    print("==== it3 start ====")
    while True:
        try:
            print(it3.__next__())
        except:
            break
    print("==== it3 finish ====")

    print("==== it4 start ====")
    while True:
        try:
            print(it4.__next__())
        except:
            break
    print("==== it4 finish ====")

    print("==== it5 start ====")
    while True:
        try:
            print(it5.__next__())
        except:
            break
    print("==== it5 finish ====")

class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self         # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

    def __getitem__(self, index):  # 해당 인덱스의 값 반환
        if index < self.stop:
            return index * 10
        else:
            raise IndexError

if __name__ == "__main__":
    iter_example1()

    for i in Counter(3):
        print(i, end=' ')

    temp = Counter(3)  # __iter__ test
    for _ in range(10):
        next(temp)

    print(f'\n{Counter(3)[1]}')