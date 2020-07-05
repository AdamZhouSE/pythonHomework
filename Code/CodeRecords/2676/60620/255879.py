t=int(input())
for i in range(t):
    result=[]
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for j in range(n-k+1):
        result.append(sum(a[j:j+k]))
    print(max(result))
