def main():
    num = int(input())

    while True:
        if num == 0:
            print(True)
            break
        else:
            if num % 3 != 0:
                print(False)
                break
            else:
                num = num / 3


if __name__ == "__main__":
    main()
