arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list1=[int(n) for n in newarr.split(',')]
arr2=input()
newarr2=""
for i in range(1,len(arr2)-1):
    newarr2=newarr2+arr2[i]
list2=[int(n) for n in newarr2.split(',')]
num=[]
for i in range(0,len(list2)):
    num.append(list2[i])
    for j in range(0,len(list1)):
        if list1[j]==list2[i]:
            num.append(list1[j])
            list1[j]=-1
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
for i in range(0,len(list1)):
    if list1[i]==-1:
        continue
    else:
        num.append(list1[i])
print(num)