num=int(input())
array=[]
length=0
for i in range(num):
    temp=input().split()
    start=int(temp[0])
    end=int(temp[1])
    height=int(temp[2])
    array.append([start,end,height])
    if end+1>length:
        length=end+1
buildings=[0]*length
for item in array:
    for i in range(item[0],item[1]):
        buildings[i]=max(buildings[i],item[2])
count=0
for item in buildings:
    count=count+item
print(count)