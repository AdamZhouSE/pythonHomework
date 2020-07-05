list=input()
res=[]
ress=[]
for i in list:
    if i not in res:
        res.append(i)
    else:
        ress.append(i)
a=[]
for i in list:
    a.append(int(i))
for i in range(1,len(list)+1):
    if i not in a:
        ress.append(i)
print(ress)