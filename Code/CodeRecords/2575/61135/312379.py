inp=list(input())
dep=0
res=list(0 for i in range(len(inp)))
for i in range(0,len(inp)):
    if inp[i]=="(":
        dep=dep+1
        if (dep%2==0): 
            res[i]=1
    else:
        if(dep%2==0):
            res[i]=1
        dep=dep-1
print(res)