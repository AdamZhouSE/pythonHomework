t = int(input())
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
for i in range(t):
    n, m, l, r = map(int, input().split())
    z=m
    x = list(map(int, input().split()))
    y = set(x)
    num = []
    for j in y:
        num.append([j, x.count(j)])
    num = sorted(num, key=lambda k: k[1])
    for j in range(l,r+1):
        if j not in y:
            num.append([j,1])
            num = sorted(num, key=lambda k: k[1])
            m-=1
            if(m==0):
                break
    h=m
    if(m!=0):
        for k in range(h):
            for j in range(len(num)):
                if(num[j][0] in range(l,r+1)):
                    num[j][1]+=1
                    m-=1
                    num = sorted(num, key=lambda k: k[1])
                    break
    fa=1
    for j in range(len(num)):
        fa=fa*f(num[j][1])
    answer=f(n+z)//fa
    print(answer)