def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    res = 10
    con = 9
    for i in range(1, n):
        res += con * (10 - i)
        con *= (10 - i)
    return res

if __name__ == '__main__':
    n = int(input())
    print(countNumbersWithUniqueDigits(n))