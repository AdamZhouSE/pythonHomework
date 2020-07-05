size=int(input())
list=input().split()
sizen=0
list1=[]
for i in range(size):
    list[i]=int(list[i])
    if list[i]!=0:
        sizen=sizen+1
for i in range(size):
    if(list[i]!=0):
        list1.append(list[i])
list1.sort()
if(sizen!=0):
    count=1
    for i in range(sizen-1):
        if list1[i]!=list1[i+1]:
            count=count+1
else:
    count=0
print(count)