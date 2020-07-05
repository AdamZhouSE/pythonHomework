inp=input()
res=1
front=inp[0]
for i in range(1,len(inp)):
    if(inp[i]!=front):
        res+=1
        front=inp[i]
if(inp[len(inp)-1]=='1'):
    res-=1
print(res,end="")
