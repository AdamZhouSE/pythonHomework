t=int(input())
res=[]
for i in range(t):
    length=int(input())
    str=input()
    isFind=False
    for j in range(len(str)):
        isIndep=True
        for k in range(len(str)):
            if k!=j and str[k]==str[j]:
                isIndep=False
        if isIndep:
            isFind=True
            res.append(str[j])
            break
    if isFind==False:
        res.append(-1)
for e in res:print(e)