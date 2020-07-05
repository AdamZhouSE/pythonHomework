list=input().split()
size1=int(list[0])
size2=int(list[1])
list1=input().split()
list2=input().split()
for i in range(size1):
    list1[i]=int(list1[i])
for i in range(size2):
    list2[i]=int(list2[i])
count=0
for i in range(size2-1):
    for j in range(size1):
        if list1[j]<=list2[i]:
            count=count+1
    print(count,end=' ')
    count=0
for j in range(size1):
        if list1[j]<=list2[size2-1]:
            count=count+1
print(count)