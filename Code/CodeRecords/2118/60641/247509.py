def main():
    num = int(input())

    while True:
        if num == 3:
            print(True)
            break
        elif num < 3:
            print(False)
            break
        elif num % 3 != 0:
            print(False)
            break
        else:
            num = num / 3


if __name__ == "__main__":
    main()
