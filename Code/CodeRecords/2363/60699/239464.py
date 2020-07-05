num=int(input())
list1=[]
if num==0:
    list1.append(0)
while num>0:
    list1.append(num%2)
    num//=2

list2=[]
for i in list1:
    if i==0:
        list2.append(1)
    else:
        list2.append(0)
res=0
index=1
for i in list2:
    res+=index*i
    index*=2
print(res)