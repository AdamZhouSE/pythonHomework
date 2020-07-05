n=int(input())
res=[]
for _ in range(n):
    res.append(input().split(" "))
for h in res:
    exp=int(h[1])
    result=pow(2,exp)-1
    result=result-int(h[0])+1
    print(result)