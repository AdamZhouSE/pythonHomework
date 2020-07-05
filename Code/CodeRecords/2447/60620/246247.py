m,n=map(int,input().split())
number=list(map(int,input().split()))
result=[]
for i in range(n):
    begin,end=map(int,input().split())
    x=min(number[(begin-1):(end)])
    result.append(x)
print(*result,end=" ")
        