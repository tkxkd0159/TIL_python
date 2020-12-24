import random

def io_test():
    with open('./Basic_Grammar/file_io/vocabulary.txt', 'w', encoding="UTF-8") as file:
        while True:
            end_sig = ["q", "ㅂ"]
            words = input("영어 단어를 입력하세요: ")
            if words in end_sig:
                break
            meaning = input("한국어 뜻을 입력하세요: ")
            file.write(f'{words} : {meaning}\n')

def word_test():
    with open('./Basic_Grammar/file_io/vocabulary.txt', 'r', encoding="UTF-8") as file:
        for lines in file:
            lines = lines.strip().split(" : ")
            eng_word = lines[0]
            kor_word = lines[1]
            ans = input(f'{kor_word}: ')
            if ans in ['q', 'ㅂ']:
                break
            if ans == eng_word:
                print("맞았습니다!")
            else:
                print(f"아쉽습니다. 정답은 {eng_word}입니다.")

def word_test_random():
    with open('./Basic_Grammar/file_io/vocabulary.txt', 'r', encoding="UTF-8") as file:
        word_dict = {}
        dict_idx = 0
        for lines in file:
            lines = lines.strip().split(" : ")
            eng_word = lines[0]
            kor_word = lines[1]
            word_dict[dict_idx] = {kor_word:eng_word}
            dict_idx += 1

    while True:
        pick_idx = random.randrange(0, len(word_dict))

        for key, value in word_dict[pick_idx].items():
            kor = key
            eng = value

        ans = input(f'{kor}: ')
        if ans in ['q', 'ㅂ']:
            print("program over")
            break

        if ans == eng:
            print("정답")
        else:
            print(f'오답, 정답은 {eng}')



def input_test():

    count = 0
    lives = 4
    ans = random.randrange(1,21)
    for _ in range(0, lives):
        res = int(input(f'기회가 {lives}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요\n'))
        count += 1
        lives -= 1
        if res == ans:
            print(f'축하합니다. {count}번만에 숫자를 맞히셨습니다.')
            break
        else:
            if res >= ans:
                print("Down")
            else:
                print("Up")

        if lives == 0:
            print(f'아쉽습니다. 정답은 {ans}였습니다.')

if __name__ == "__main__":
    word_test_random()
