temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
res=[]
def findMax(li):
    mos=max(li)
    return li.index(mos)

for i in range(len(temp),1,-1):
    ind=findMax(temp[0:i])
    pre=temp[0:ind+1]
    pre.reverse()
    now=pre+temp[ind+1:i]
    now.reverse()
    temp=now+temp[i:]
    if((ind+1)!=1):
        res.append(ind+1)
    res.append(i)
    
print(res)