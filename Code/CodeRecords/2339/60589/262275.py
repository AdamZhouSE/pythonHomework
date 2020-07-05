t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split(' ')))
    cnt=0
    for x in range(n):
        for y in range(x+1,n):
            if a[x]>a[y]:
                cnt+=1
    print(cnt)