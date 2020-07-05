src1=input()[1:-1]
src2=input()[1:-1]
li1=src1.split(',')
li2=src2.split(',')
res=[]
for n in li1:
    if n!='null' and n!='':
        res.append(int(n))
for n in li2:
    if n!='null' and n!='':
        res.append(int(n))
res.sort()
print(res)