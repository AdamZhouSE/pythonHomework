tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
d=int(tmp[2])
list1=[]
for i in range(0,n):
    tmp=input().split()
    for j in tmp:
        list1.append(int(j))
list1.sort()
std=list1[0]%d
list2=[]
flag=1
for i in list1:
    if i%d!=std:
        flag=0
    else:
        list2.append(int(i/d))
if flag==0:
    print(-1)
else:
    minn=2**10
    for i in list2:
        summ=0
        for j in list2:
            summ+=abs(i-j)
        minn=min(minn,summ)
    print(minn)