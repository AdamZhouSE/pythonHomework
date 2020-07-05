t=int(input())
for nn in range(t):
    n=int(input())
    li=list(eval(input().replace(' ',',')))
    res=0
    for i in li:
        if i-1 not in li:
                y = i +1
                while y in li:
                    y += 1
                res = max(res, y - i)
    print(res)