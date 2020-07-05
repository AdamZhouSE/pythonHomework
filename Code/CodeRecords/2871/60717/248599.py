n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
count=0
while 2 in list1 and 1 in list1:
    count+=1
    list1.remove(1)
    list1.remove(2)
if 2 in list1:
    print(count)
else:
    print(int(len(list1)/3)+count)