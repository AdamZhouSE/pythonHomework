cnt=input()
list1=[int(e) for e in input().split(' ')]
list2=[]
res=0
for i in list1:
    if i%2==0:
        res+=i
    else:
        list2.append(i)
list2.sort()
if len(list2)%2==0:
    for i in list2:
        res+=i
else:
    for i in range(1,len(list2)):
        res+=list2[i]
print(res)

