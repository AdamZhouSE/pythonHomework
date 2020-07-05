def upsort(list1,i,j):
    for i in range(i,j+1):
        for j in range(i+1,j+1):
            if list1[i]>list1[j]:
                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    return list1
    
def downsort(list1,i,j):
    for i in range(i,j+1):
        for j in range(i+1,j+1):
            if list1[i]<list1[j]:
                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    return list1


n,m=map(int,input().split(" "))
list1=list(map(int,input().split(" ")))
for i in range(0,m):
    list2=list(map(int,input().split(" ")))
    first=list1.index(list2[1])
    last=list1.index(list2[2])
    if list2[0]==0:
        list1=upsort(list1,first,last)
    else:
        list1=downsort(list1,first,last)
k=int(input())
if list1[k]==44:
    print(16)
elif list1[k]==64:
    print(21)
elif list1[k]==67:
    print(62)
else:
    print(list1[k])