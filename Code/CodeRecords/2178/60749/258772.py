

n=int(input())
res=list(map(int,input().split(" ")))
def countsub(numarray):
    res=[]
    for h in range(1,len(numarray)+1):
        for x in range(0,len(numarray)-h+1):
            res.append(numarray[x:x+h])
    res=getnorepeat(res)

    return len(res)
def getnorepeat(res):
    result=[]
    for t in res:
        if t not in result:
            result.append(t)
    return result

temp=[]
for t in range(0,len(res)):
    temp.append(res[t])
    print(countsub(temp))