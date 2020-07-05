s=list(eval(input()))
res=[]
tmp=s
while len(tmp)!=1:
    maxNum=0
    for i in tmp:
        if(i>maxNum):
            maxNum=i
    index=0
    for i in range(len(tmp)):
        if tmp[i]==maxNum:
            index=i
            break
    if(index+1!=1):
        res.append(index+1)
    k=tmp[:index + 1]
    k.reverse()
    for i in tmp[index+1:]:
        k.append(i)
    tmp=k
    res.append(len(tmp))
    tmp.reverse()
    tmp=tmp[:len(tmp)-1]
print(res)