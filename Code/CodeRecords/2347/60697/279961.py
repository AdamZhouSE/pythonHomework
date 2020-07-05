import sys
import collections
t=input()
res=[]
anss=[]
tmp=collections.defaultdict(list)
for line in sys.stdin:
    b=line.split(' ')
    a=[]
    for i in b:
        if(i!='' and i!='\n'):
            a.append(int(i))
    res.append(a)
    tmp[a[0]].append(a[1])
    tmp[a[1]].append(a[0])
tmp2=sorted(tmp.items(),key=lambda x:len(x[1]))
for i in range(len(tmp2)):
    tmp2[i]=list(tmp2[i])
for i in range(len(tmp2)):
    tmp2[i][1].sort(key=lambda x:len(tmp[x]))

for item in tmp2:
    a=item[0]
    b=item[1]
    if(a not in anss):
        for i in b:
            if(i not in anss):
                anss.append(i)
                anss.append(a)
                break
print(len(anss)//2)




