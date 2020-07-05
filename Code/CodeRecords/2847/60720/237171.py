size=int(input())
list1=input().split()
list2=input().split()
s=int(list2[0])
e=int(list2[1])
count=0
for i in range(size-1):
    list1[i]=int(list1[i])
for i in range(s-1,e-1):
    count+=list1[i]
print(count)