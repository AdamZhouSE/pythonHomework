T=int(input())
res=[]
for a in range(T):
    inp=int(input())
    numslist = (input().split(" "))
    numslist=list(int(x) for x in numslist)
    temp=0
    for j in range(inp-1):
        for k in range(j+1,inp):
            if numslist[j]==numslist[k]:
                temp+=1
    res.append(temp)
for i in res:
    print(i)