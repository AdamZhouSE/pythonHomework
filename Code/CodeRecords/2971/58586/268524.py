line=input()
res=[]
for step in range(len(line)-1,-1,-1):
    res.append((line[step:],step+1))
res.sort(key=lambda x:x[0])
ans=[]
for c in res:
    ans.append(c[1])
print(*ans,end=" ")
