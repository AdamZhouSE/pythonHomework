t=int(input())
for i in range(t):
    result=[]
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(n):
        if(a[j]==max(a[j:n])):
            result.append(a[j])
    print(*result)