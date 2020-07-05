T = eval(input())
for i in range(T):
    n1, n2 = [int(x) for x in input().split()]
    n1 -= 1
    n2 -= 1
    res = 1
    big = n1+n2
    small = min(n1, n2)
    for j in range(small):
        res *= big
        big -= 1
    for j in range(small):
        res //= (j+1)
    print(res)
