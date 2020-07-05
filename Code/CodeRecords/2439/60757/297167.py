def judge(arr1,arr2,u,v):
    while(u!=v):
        if arr1.count(u)==0:
            return False
        ind=arr1.index(u)
        if v==arr2[ind]:
            return True
        u=arr2[ind]
    return False
n=int(input())
arr1=[]
arr2=[]
arr3=[]
for i in range(n-1):
    li=input().split()
    arr1.append(int(li[0]))
    arr2.append(int(li[1]))
    arr3.append(int(li[2]))
m=int(input())
for i in range(m):
    li=input().split()
    u=int(li[0])
    v=int(li[1])
    count=0
    if not(judge(arr1,arr2,u,v)):
        tmp=u
        u=v
        v=tmp
    while(True):
        if arr1.count(u)==0:
            count=0
            break
        ind=arr1.index(u)
        count=count^arr3[ind]
        if v==arr2[ind]:
            break
        u=arr2[ind]
    print(count)