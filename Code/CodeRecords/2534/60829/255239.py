a=list(input())
aa=[]
for i in a:
    if i<='9' and i>='0':
        aa.append(int(i))
aa.sort()
print(aa)