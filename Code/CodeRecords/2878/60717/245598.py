import sys
list1=input().split()
n=int(list1[0])
k=int(list1[1])
list2=input().split()
for i in range(0,n):
    list2[i]=int(list2[i])
list2.sort()
output=sys.maxsize
for i in list2:
    if k%i==0:
        output=min(output,int(k/i))
print(output)