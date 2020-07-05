s=list(eval(input()))
k=list(eval(input()))
tmp=[]
d=[]
for i in s:
    if i not in k :
        tmp.append(i)
tmp.sort()
for i in k:
    for z in s:
        if z==i :
            d.append(i)
for i in tmp:
    d.append(i)
print(d)