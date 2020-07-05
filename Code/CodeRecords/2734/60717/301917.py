tmp=input().split()
n=int(tmp[0])
c=int(tmp[1])
m=int(tmp[2])
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
for i in range(0,m):
    tmp=input().split()
    l=int(tmp[0])
    r=int(tmp[1])
    tmp=[]
    tmp1=[]
    for j in range(l-1,r):
        if not list1[j] in tmp:
            tmp.append(list1[j])
        elif list1[j] in tmp and (not list1[j] in tmp1):
            tmp1.append(list1[j])
    print(len(tmp1))