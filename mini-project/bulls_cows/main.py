from random import randint

def pick_startnum():
    numlist = []

    while len(numlist) < 3:
        rnd_num = randint(0, 9)
        if rnd_num not in numlist:
            numlist.append(rnd_num)

    return numlist


def main():
    print(pick_startnum())



if __name__=="__main__":
    main()