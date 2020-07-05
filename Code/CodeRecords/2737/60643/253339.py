l=input()
time=len(l)//3
res=[]
temp=[]#为了去重
for i in l:
    if i not in temp:
        temp.append(i)
        n=l.count(i)
        if n>time:
            res.append(i)
    else:
        continue
print(res)