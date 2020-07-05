m,n=tuple(map(int,input().split()))
bill=list(map(int,input().split()))
ans=[]
for i in range(n):
    a,b=tuple(map(int,input().split()))
    ans.append(str(min(bill[a-1:b])))
for i in ans:
    print(i+" ",end="")