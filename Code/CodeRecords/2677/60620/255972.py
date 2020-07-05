t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    num=0
    for j in range(n):
        for k in range(j+1,n):
            if(a[j]==a[k]):
                num+=1
    print(num)