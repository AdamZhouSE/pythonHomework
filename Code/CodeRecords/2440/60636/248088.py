res=[]
source=eval(input())
for i in source:
    print(i)
    if(len(res)==0):
        res.append(i)
    else:
        x=len(res)
        for a in range(x):
            if(i<=res[a]):
                res.insert(a,i)
                break
        if(len(res)==x):
            res.pop(i)
print(res)