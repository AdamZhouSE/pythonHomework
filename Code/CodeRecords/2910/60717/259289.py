n=int(input())
list1=input().split()
maxx=max(int(list1[0]),int(list1[1]))
flag=1
for i in range(0,n-1):
    list1=input().split()
    tmp1=max(int(list1[0]),int(list1[1]))
    tmp=min(int(list1[0]),int(list1[1]))
    if tmp1<=maxx:
        maxx=tmp1
    elif tmp>maxx:
        flag=0
    else:
        maxx=tmp
if flag==0:
    print('NO')
else:
    print('YES')