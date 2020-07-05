def main():
    n = int(input())
    for i in range(0, n):
        num_1, num_2 = map(int, input().split(" "))
        result = -1
        if num_1 != num_2:
            result = 1
            while num_1 > 0 or num_2 > 0:
                if num_1 % 2 != num_2 % 2:
                    break
                else:
                    num_1 = (num_1 - num_1 % 2) / 2
                    num_2 = (num_2 - num_2 % 2) / 2
                    result += 1
        else:
            result = -1
        print(result)


if __name__ == '__main__':
    main()
