lists=eval(input())

def insertToList(x,res):
    if len(res)==0:
        res.append(x)
        return res
    a=True
    for i in range(0,len(res)):
        if res[i]>x:
            res.insert(i,x)
            a=False
            break
    if a:
        res.append(x)
    return res

res=[]
for i in range(0,len(lists)):
    temp=lists[0]
    lists.remove(temp)
    res=insertToList(temp,res)

print(res)