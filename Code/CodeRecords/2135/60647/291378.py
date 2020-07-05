list=input().split(',')
list.sort()
all=0
for i in list:
    all+=int(i)
all=int(all/len(list))
temp=all
for i in range(len(list)):
    if int(abs(all-int(list[i])))<=int(temp):
        temp=int(abs(all-int(list[i])))
res=0
aa=int(abs(all-temp))
for i in range(len(list)):
    res+=int(abs(aa-int(list[i])))
if len(list)==3:
    ressa=int(list[2])-int(list[0])
if ressa<=res:
    print(ressa)
else:
    print(res)