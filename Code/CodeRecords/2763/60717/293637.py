def fuc(list1,list2,m,n):
    floor=list2[0]
    count=list2[1]
    while list1[floor]<m:
        if floor!=n-1:
            list1[floor+1]=2*list1[floor]
            list2[0]+=1
            fuc(list1,list2,m,n)
            list1[floor]+=1
        else:
            list2[1]+=1
            list1[floor]+=1
    if list1[floor]==m and floor==n-1:
        list2[1]+=1
    list2[0]-=1
    return

a=int(input())
for i in range(0,a):
    tmp=input().split()
    m=int(tmp[0])
    n=int(tmp[1])
    list1=[0 for j in range(0,n)]
    list1[0]=1
    list2=[0,0]
    fuc(list1,list2,m,n)
    print(list2[1])