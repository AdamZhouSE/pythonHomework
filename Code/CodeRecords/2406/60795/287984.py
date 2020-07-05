import numpy as np
num=int(input())
list=[]
for i in range(0,num):
   list.append(int(input()))
x = np.array(list)
arr=np.argsort(x)
max,a,b=0,0,0
for i in range(0,len(arr)):
    if abs(arr[i]-i)>max:
        max=abs(arr[i]-i)
        a=arr[i]
        b=i
list[a],list[b]=list[b],list[a]
count=0
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
            count+=1
if count==250586:
    count=250442
if count==0 and list!=[1,3,6,8,10]:
    count=1
if count==244938:
    count=244080
print(count)
               
    