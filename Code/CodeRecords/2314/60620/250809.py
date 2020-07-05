n=int(input())
result=[]
for i in range(n):
    fa,lch,rch=input().split()
    if fa in result:
        index=result.index(fa)
    else:
        if(lch!='0'):
            result.append(lch)
        if(fa!='0'):
            result.append(fa)
        if(rch!='0'):
            result.append(rch)
            continue
    if(lch!='0'):
        result.insert(index,lch)
        index+=1
    if(rch!='0'):
        result.insert(index+1,rch)
print(*result,end=" ")