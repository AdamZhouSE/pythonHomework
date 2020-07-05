def main():
    num = input()
    if num[0] == "-":
        print(int("-" + num[:0:-1]))
    else:
        print(int(num[::-1]))


if __name__ == '__main__':
    main()
