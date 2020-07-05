lists=eval("["+input()+"]")
res=0

for k in range(0,len(lists)):
    newLists=[]
    for i in range(0,len(lists)):
        newLists.append(lists[i]*i)
    lists=lists[len(lists)-1:]+lists[0:len(lists)-1]
    res=max(res,sum(newLists))

print(res)