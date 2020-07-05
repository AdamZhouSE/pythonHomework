n=int(input())
res=[]
for _ in range(n):
    k=int(input())
    nums=list(map(int, input().split(" ")))
    temp=1
    for h in nums:
        temp=temp*h
    ans=[]
    for h in nums:
        ans.append(temp//h)
    res.append(ans)
for t in res:
    for h in t:
        print(str(h)+" ", end="")
    print()