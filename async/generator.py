def three_generator():
    a = [1, 2, 3]
    yield from a

def three_generator2():
    yield 1
    yield 2
    yield 3

def inf_generator():
    count = 0
    while True:
        yield count
        count += 1

if __name__ == "__main__":
    mygen = inf_generator()
    print(next(mygen))
    print(next(mygen))