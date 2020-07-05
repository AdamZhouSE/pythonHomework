def get_1s(num):
    res = 0
    tmp = num
    while tmp > 0:
        res += tmp % 2
        tmp //= 2
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        result.append(get_1s(int(input())))
    for i in range(len(result)):
        print(result[i])