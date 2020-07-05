tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
for i in range(0,m):
    list2=input().split()
    if list2[0]=='Q':
        l=int(list2[1])
        r=int(list2[2])
        k=int(list2[3])
        tmp=[]
        for j in range(l-1,r):
            tmp.append(list1[j])
        tmp.sort()
        print(tmp[k-1])
    else:
        list1[int(list2[1])-1]=int(list2[2])