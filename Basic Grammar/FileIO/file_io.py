def main():
    test_array = [2, 3, 4]
    with open('testIO.txt', 'w') as file:
        for target in test_array:
            file.write(str(target))
            file.write(" ")


if __name__ == "__main__":
    main()
