def cal(n):
    res = 0
    for i in range(1,n+1):
        res += int(pow(i,5))
    return res


t = int(input())
for i in range(t):
    n = int(input())
    print(cal(n))