a=int(input())
b=[int(i) for i in input().split()]
c=[]
index=0
maxnum=0
for i in range(0,len(b)):
    if b[i] not in c:
        index+=1
        c.append(b[i])
        if index>maxnum:
            maxnum=index
    else:
        c.remove(b[i])
        index-=1
print(maxnum)