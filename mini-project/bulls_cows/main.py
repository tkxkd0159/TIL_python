from random import randint

def pick_sol():
    numlist = []

    while len(numlist) < 3:
        rnd_num = randint(0, 9)
        if rnd_num not in numlist:
            numlist.append(rnd_num)

    return numlist

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    idx = 0

    while idx < 3:
        try:
            guess_num = int(input(f'{idx+1}번째 숫자를 입력하세요: '))
        except ValueError as err:
            print(err)
            continue

        if guess_num > 9 or guess_num < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if guess_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue

        new_guess.append(guess_num)
        idx += 1

    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for idx, _ in enumerate(solution):
        if guess[idx] == solution[idx]:
            strike_count += 1
        elif guess[idx] in solution:
            ball_count += 1


    return strike_count, ball_count


def main():
    idx = 0
    strike = 0
    while strike != 3:
        idx += 1
        sol_set = pick_sol()
        guess_set = take_guess()
        strike, ball = get_score(guess_set, sol_set)
        print(f'\nstrike : {strike}, ball : {ball}')
        print(f'Your guess is {guess_set}')
        print(f'The answer is {sol_set}\n')

    print(f'You succeed in {idx} attempts')



if __name__ == "__main__":
    main()