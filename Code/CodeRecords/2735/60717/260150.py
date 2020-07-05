tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
for i in range(0,m):
    list2=input().split()
    l=int(list2[0])
    r=int(list2[1])
    k=int(list2[2])
    tmp=[]
    for j in range(l-1,r):
        tmp.append(list1[j])
    tmp.sort()
    print(tmp[k-1])