def main():
    n = int(input())
    for i in range(0, n):
        num, length = map(int, input().split(" "))
        combinations = [[]]
        result = 0
        for j in range(1, num):
            k = len(combinations)
            for l in range(0, k):
                if len(combinations[l]) < length:
                    temp = combinations[l] + [j]
                    combinations.append(temp)
                    if sum(temp) == num and len(temp) == length:
                        result = 1
                if result == 1:
                    break
            if result == 1:
                break
        print(result)


if __name__ == '__main__':
    main()
