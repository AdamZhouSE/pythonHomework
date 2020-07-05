def main():
    n = int(input())

    while True:
        if n == 1:
            print(True)
            break
        else:
            if n % 2 is not 0:
                print(False)
                break
            else:
                n = int(n / 2)


if __name__ == "__main__":
    main()