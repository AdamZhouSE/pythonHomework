n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
list1.sort()
while list1[n-1]!=0 and list1[n-2]!=0:
    a=list1.pop()
    b=list1.pop()
    list1.append(0)
    list1.append(abs(a-b))
    list1.sort()
if list1[n-1]==0 and list1[n-2]==0:
    print('YES')
else:
    print('NO')