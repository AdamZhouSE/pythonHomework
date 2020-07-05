s=input()
li=list(eval(s))
li.sort()
res=[]
for i in range(0,len(li)):
    if i==0:
        if li[0]!=li[1]:
            res.append(li[0])
    else:
        if i<=(len(li)-2):
            if (li[i]==li[i-1]) or (li[i]==li[(i+1)]):
                continue
            else:
                res.append(li[i])
        else:
            if(i==len(li)-1):
                if(li[i]!=li[i-1]):
                    res.append(li[i])
for i in range(len(res)):
    print(res[i])