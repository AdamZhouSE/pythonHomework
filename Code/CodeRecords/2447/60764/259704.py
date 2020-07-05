m,n=map(int,input().split())
accounts=list(map(int,input().split()))
res=[]
for i in range(n):
    question=list(map(int,input().split()))
    res.append(min(accounts[question[0]-1:question[1]]))
print(' '.join(str(r) for r in res),end=" ")