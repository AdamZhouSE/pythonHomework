n = int(input())
list1=input().split()
list2=input().split()
count=0
for i in list1:
    if list1.index(i)<=list2.index(i):
        count=max(count,list2.index(i)-list1.index(i))
print(count)