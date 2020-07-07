s=list(eval(input()))
k=list(eval(input()))
res=[]
for i in s:
    if i in k:
        res.append(i)
res.sort()
print(res)