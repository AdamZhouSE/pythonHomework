n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    r=0
    for j in range(m):
        for k in range(j+1,m):
            if a[j]>a[k]:
                r+=1
    print(r)