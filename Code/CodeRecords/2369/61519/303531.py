n=int(input())
res=[]
for i in range(n):
    tem=list(input())
    root=tem[0]
    left=tem[1]
    right=tem[2]
    if root in res:
        ind=res.index(root)
    else:
        if root!="*":
            res.append(root)
        if left!="*":
            res.append(left)
        if right!="*":
            res.append(right)
        continue
    if left!="*":
        res.insert(ind+1,left)
    if right!="*" and left!="*":
        res.insert(ind+2,right)
    if right!="*" and left=="*":
        res.insert(ind+1,right)
s="".join(res)
print(s,end="")