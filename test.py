with open('vocabulary.txt', 'a', encoding="UTF-8") as f:
    while True:
        words = input("영어 단어를 입력하세요: ")
        if words == "q":
            break
        meaning = input("한국어 뜻을 입력하세요: ")
        f.write(f'{words} : {meaning}\n')
