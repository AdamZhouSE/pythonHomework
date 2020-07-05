a=list((input()))
b=list((input()))
tmp = [val for val in a if val in b]
tmp.sort()
aa=[]
for i in tmp:
    if i<='9' and i>='0':
        aa.append(int(i))
aa.sort()
print(aa)