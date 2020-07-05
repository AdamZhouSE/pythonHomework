size=int(input())
list=input().split()
for i in range(size):
    list[i]=int(list[i])
list.sort()
count=1
list1=[]
list1.append(list[0])
for i in range(size-1):
    if list[i]!=list[i+1]:
        count=count+1
        list1.append(list[i+1]) 
if count==1:
    print(0)
elif count==2:
    if (list1[1]-list1[0])%2==0:
        print(int((list1[1]-list1[0])/2))
    else:
        print(list1[1]-list1[0])
elif count==3:
    if list1[2]+list1[0]==2*list1[1]:
        print(list1[2]-list1[1])
    else:
        print(-1)
else:
    print(-1)