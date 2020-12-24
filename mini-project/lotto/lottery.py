from random import randrange


def generate_numbers(num, start, end):
    whole_list = [i for i in range(start, end+1)]
    pick_list = []
    for _ in range(num):
        get_num = whole_list.pop(randrange(0, len(whole_list)))
        pick_list.append(get_num)
    return pick_list


def draw_winning_numbers():
    init_list = generate_numbers(7, 1, 45)

    win_numlist = init_list[0:6]
    win_numlist.sort(reverse=False)
    win_numlist.append(init_list[6])
    return win_numlist


def count_match_numbers(src_list, my_list):
    count = 0
    for element in my_list:
        if element in src_list:
            count += 1
    return count


def check(src_list, my_list):

    bonus_num = src_list[6]
    count = count_match_numbers(src_list, my_list)

    if count == 6:
        if bonus_num in my_list:
            return 5*(10**7)
        else:
            return 10**9
    elif count == 5:
        return 10**6
    elif count == 4:
        return 5*(10**4)
    elif count == 3:
        return 5*(10**3)
    else:
        return 0


def main():
    win_numlist = draw_winning_numbers()
    mypick = [2, 3, 4, 5, 6, 8]
    print(check(win_numlist, mypick))


if __name__ == "__main__":
    main()
