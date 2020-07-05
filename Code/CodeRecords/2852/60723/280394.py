n=int(input())
temp=input().split()
array=[]
for i in range(n):
    array.append(int(temp[i]))
num=0
count=[]
while num<n:
    temp=0
    while num<n and array[num]==2:
        temp=temp+1
        num=num+1
    if temp!=0:
        count.append(temp)
    temp=0
    while num<n and array[num]==1:
        temp=temp+1
        num=num+1
    if temp!=0:
        count.append(temp)
result=[]
for i in range(len(count)-2):
    temp=count[i:i+3]
    result.append(min(max(temp[0],temp[2]),temp[1]))
print(max(result)*2)