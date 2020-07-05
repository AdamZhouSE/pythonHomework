n=int(input())
list1=input().split()
maxx=max(int(list1[0]),int(list1[1]))
flag=1
for i in range(0,n):
    list1=input().split()
    tmp=min(int(list1[0]),int(list1[1]))
    if tmp>maxx:
        flag=0
if flag==0:
    print('NO')
else:
    print('YES')