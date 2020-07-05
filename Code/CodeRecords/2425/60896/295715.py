def find(list1,n,x):
    if(list1[0]>=x):
        return 0
    for i in range(1,n):
        if(list1[i]>x):
            return i
    return n

a=eval(input())
for i in range(0,a):
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    n=list1[0]
    x=list1[1]
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    index=find(list1,n,x)
    if(index==n):print(list1[-1])
    if(index==0):print(list1[0])
    else:
        if(list1[index]-x<=x-list1[index-1]):
            print(list1[index])
        else:
            print(list1[index-1])