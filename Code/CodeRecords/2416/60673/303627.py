def doInstrs(instrs,drums,i):
    if(drums[instrs[i]-1]==1):drums[instrs[i]-1]=0
    else:drums[instrs[i]-1]=1
    return drums

def findMax(drums):
    res=[]
    s,e=0,1
    for i in range(len(drums)-1):
        if(drums[i]==drums[e]):
            s=i+1
            e=s+1
        else:
            l=e-s+1
            res.append(l)
            e+=1
    return(max(res))
            
def findLongest(n,instrs):
    drums=[1 for i in range(n)]
    for i in range(len(instrs)):
        drums=doInstrs(instrs,drums,i)
        print(findMax(drums))

inp=input().split(" ")
n,m=int(inp[0]),int(inp[1])
instrs=[]
for i in range(m):
    instrs.append(int(input()))
findLongest(n,instrs)
