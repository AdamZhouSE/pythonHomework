l=eval(input())
res=[]
bound=len(l)-1
for i in range(len(l)-1):
    tmp=l.index(max(l))
    if tmp==bound:
        l=l[:-1]
        continue
    if tmp!=0:
        l = l[tmp::-1] + l[tmp + 1:]
        res.append(tmp + 1)
    res.append(len(l))
    l=l[:0:-1]
print(res)