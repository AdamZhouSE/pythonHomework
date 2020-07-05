s=list(eval(input()))
res=[]
tmp=[]
for i in s:
    if(i%2==0):
        res.append(i)
    else:tmp.append(i)
for i in tmp:
    res.append(i)
print(res)