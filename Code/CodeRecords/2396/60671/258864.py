length=int(input())
str0=input()
ll=str0.split()
list0=[]
for i in ll:
    list0.append(int(i))

pla=[]

for i in range(length):
    needToSort=list0[i:]
    dontNeedToSort=list0[:i]
    
    minnum=needToSort[0]
    for j in needToSort:
        minnum=min(minnum,j)
    
    minplace=needToSort.index(minnum)
    
    pla.append(minplace+i+1)
    
    inner=needToSort[:minplace+1]
    outer=needToSort[minplace+1:]
    
    inner.reverse()
    
    
    list0=dontNeedToSort+inner+outer

print(*pla,end=' ')