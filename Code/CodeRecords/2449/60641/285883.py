def main():
    string = input()
    nums = eval(string.split("=")[1][1:len(string.split("=")[1]) - 9])
    key = int(string.split("=")[2])
    try:
        print(nums.index(key))
    except ValueError:
        print(-1)


if __name__ == '__main__':
    main()
