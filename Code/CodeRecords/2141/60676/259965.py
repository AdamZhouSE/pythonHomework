def transformer(num):
    res = ''
    tmp = num
    while tmp > 0:
        res = str(tmp % 2) + res
        tmp //= 2
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        n = int(input())
        tmp = []
        for j in range(n):
            tmp.append(transformer(j+1))
        result.append(tmp)
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=' ')
        print()