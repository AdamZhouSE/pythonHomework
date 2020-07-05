def solve(num1, num2):
    num = [0 for i in range(len(num1) + len(num2))]
    for i in range(len(num1) - 1, -1, -1):
        t = ord(num1[i]) - ord('0')
        for j in range(len(num2) - 1, -1, -1):
            temp = t * (ord(num2[j]) - ord('0'))
            num[i + j + 1] += temp % 10
            num[i + j] += num[i + j + 1] % 10 + int(temp / 10)
            num[i + j + 1] %= 10
    res = ''
    i = 0
    while num[i] == 0:
        i += 1
    while i < len(num):
        res += str(num[i])
    return res


if __name__ == '__main__':
    num1 = input()
    num2 = input()
    print(solve(num1, num2))