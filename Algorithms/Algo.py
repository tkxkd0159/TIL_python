import math
TMPLIST = [1, 2, 3, 4, 5, 6, 7, 8]


def bin_search(list_, item):
    low = 0
    high = len(list_) - 1
    cnt = 0

    while low <= high:
        mid = (low+high) // 2
        guess = list_[mid]
        cnt += 1
        if guess == item:
            return mid, cnt
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(bin_search(TMPLIST, 8))
print(math.log(8, 2))
