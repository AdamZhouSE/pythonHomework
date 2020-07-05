size=int(input())
list1=input().split()
list=[]
count=1
for i in range(size):
    list1[i]=int(list1[i])
for i in range(1,size):
    if list1[i]==1:
        list.append(list1[i-1])
        count=count+1
print(count)
for index in list:
    print(index,end=' ')
print(list1[size-1])