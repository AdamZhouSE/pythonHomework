list=input().split()
size=int(list[0])
d=int(list[1])
count=0
list1=input().split()
for i in range(size-1):
    list1[i]=int(list1[i])
    list1[i+1]=int(list1[i+1])
    while(list1[i+1]<=list1[i]):
        list1[i+1]+=d
        count=count+1
print(count)