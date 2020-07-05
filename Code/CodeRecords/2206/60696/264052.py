def f(n):
    res = 0
    j = 1
    for i in range(1,n+1):
        temp = 1
        for k in range(1,i+1):
            temp *= j
            j += 1
        res += temp
    return res


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(f(num))