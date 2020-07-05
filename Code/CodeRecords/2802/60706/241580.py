list=input().split(' ')
n=int(list[0])
m=int(list[1])
num=[]
k=int(0)
id=int(0)
t=0
id=[]
list2=input().split(' ')
for i in range(0,n):
    num.append(int(list2[i]))
for i in range(1,n+1):
    id.append(i)
temp=0
id_temp=0
i=0
while len(num)>1:
    if num[0]>m:
        temp=num[0]
        del(num[0])
        num.append(temp-m)
        id_temp=id[0]
        del(id[0])
        id.append(id_temp)
    else:
        del(num[0])
        del(id[0])
print(id[0])