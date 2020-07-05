lst0=input().split()
n=int(lst0[0])
m=int(lst0[1])
list0=[0]*n
for k in range(m):
    list1=input().split()
    t=int(list1[1])
    g=int(list1[2])
    if list1[0]=='0':
        for i in range(t-1,g):
            if list0[i]==0:
                list0[i]=1
            else:
                list0[i]=0
    else:
        sum=0
        for i in range(t-1, g ):
            if list0[i]==1:
                sum+=1
        print(sum)
