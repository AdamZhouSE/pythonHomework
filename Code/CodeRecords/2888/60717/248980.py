list1=input().split()
n=int(list1[0])
m=int(list1[1])
list1=input().split()
pCount=0
nCount=0
for i in range(0,n):
    list1[i]=int(list1[i])
    if list1[i]>0:
        pCount+=1
    if list1[i]<0:
        nCount+=1
for i in range(0,m):
    list1=input().split()
    l=int(list1[0])
    r=int(list1[1])
    if (r-l)%2==0:
        print(0)
    elif int((r-l+1)/2)<=pCount and int((r-l+1)/2)<=nCount:
        print(1)
    else:
        print(0)
        

