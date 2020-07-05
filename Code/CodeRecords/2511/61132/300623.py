t,k = map(int,input().split())
l=[]
ans=[]
for j in range(t):
    l.append(int(input()))
for i in range(len(l)):
    for le in range(len(l)-i,1,-1):
        if le%2==0 and sum(l[i:i+le//2])<=k and sum(l[i+le//2:i+le])<=k:
            ans.append(le)
            break
    else:
        ans.append(0)
for i in ans:
    print(i)