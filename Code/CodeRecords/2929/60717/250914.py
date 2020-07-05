list1=input().split()
n=int(list1[0])
m=int(list1[1])
list2=[]
list3=[]
list4=[]
for i in range(0,n):
    list1=input().split()
    a=int(list1[0])
    b=int(list1[1])
    list2.append(a)
    list3.append(b)
    list4.append(a-b)
flag=0    
for i in list3:
    flag+=i
flag1=0
for i in list2:
    flag1+=i
if flag>m:
    print(-1)
elif flag1<=m:
    print(0)
else:
    count=n+1

    while flag<=m:
        flag+=min(list4)
        list4[list4.index(min(list4))]=m
        count-=1
    if count<0:
        print(0)
    else:
        print(count)
        
    