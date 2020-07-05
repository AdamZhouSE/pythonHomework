info=input().split(',')
a=[int(y) for y in info]
K=int(input())
a.sort()
if len(a)==1:
    print(0)
else:
    if a[0]+K>=a[-1]-K:
        print(0)
    else:
        print((a[-1]-K)-(a[0]+K))