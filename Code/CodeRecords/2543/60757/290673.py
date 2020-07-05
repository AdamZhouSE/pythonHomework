t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    re=[]
    for j in range(1,n+1):
        re1=[]
        for k in range(len(li)-j+1):
            re2=[]
            for l in range(j):
                re2.append(li[k+l])
            re1.append(min(re2))
        re.append(max(re1))
    for j in range(len(re)-1):
        print(re[j],end=' ')
    print(re[len(re)-1])