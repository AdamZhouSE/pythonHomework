def l(num,c,sum,re):
    if num >= c.__len__():
        re.append(sum)
        return
    else:
        l(num+1,c,sum,re)
        sum+=c[num]
        l(num+2,c,sum,re)
a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    re = []
    l(0, c, 0, re)
    re.sort()
    print(re[-1])