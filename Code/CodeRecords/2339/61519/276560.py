n=int(input())
for j in range(n):
    res=0
    m=int(input())
    num=list(input().split(" "))
    for i in range(m):
        num[i]=int(num[i])
    for k in range(m-1):
        for l in range(k+1,m):
            if num[k]>num[l]:
                res=res+1
    print(res)