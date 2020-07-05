lst0=input().split()
n=int(lst0[0])
p=int(lst0[1])
list0=input().split()
list0=[int(list0[i]) for i in range(n)]
m=int(input())
for k in range(m):
    list1=input().split()
    t=int(list1[1])
    g=int(list1[2])
    if(list1[0]!='3'):
        c=int(list1[3])
    if list1[0]=='1':
        for i in range(t-1,g):
            list0[i]=c*list0[i]
    elif list1[0]=='2':
        for i in range(t-1, g ):
            list0[i] += c
    else:
        sum=0
        for i in range(t-1, g ):
            sum+= list0[i]
        print(sum%p)
