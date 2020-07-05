def prim(nu):
    d = 2
    flag = 1
    while d < nu:
        if nu % d == 0:
            flag = 0
        d = d + 1
    return flag


t = int(input())
res = []
for i in range(t):
    n = int(input())
    num = 2
    while n > 0:
        if prim(num) == 1:
            n -= 1
        num += 1
        if n == 0:
            res.append(pow(num - 1,2)+1)
for i in res:
    print(i)
    