def f(n):
    cnt = 1
    value = 0
    for i in range(1,n+1):
        tmp = cnt
        for j in range(cnt+1,cnt+i):
            tmp = tmp * j
        value = value + tmp
        cnt = cnt + i
    return value


num = int(input())
for i in range(num):
    a = int(input())
    print(f(a))