import itertools
list=input()
k=int(list[0])
n=int(list[1])
list1=[1,2,3,4,5,6,7,8,9]
list=[]
a=[]
for i in itertools.combinations(list1,k):
    list.append(i)
for i in list:
    sum=0
    for j in i:
        sum=sum+j
    if sum==n:
        a.append(i)
res=[]
for i in a:
    list=[]
    for j in i:
        list.append(j)
    res.append(list)
print(res)