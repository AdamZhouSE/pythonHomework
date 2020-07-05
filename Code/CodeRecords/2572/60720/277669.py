lst0=input().split()
n=int(lst0[0])
t=int(lst0[1])
m=int(lst0[2])
list0=[1]*n
for k in range(m):
    list1=input().split()
    a=int(list1[1])
    b=int(list1[2])
    if a>b:
        temp=a
        a=bb=temp
    list2=[a,b]
    tn=0
    if(list1[0]=='C'):
        tn=int(list1[3])
    if list1[0]=='C':
        for i in range(a-1,b):
            list0[i]=tn
    else:
        list3=[]
        for i in range(a-1,b):
            list3.append(list0[i])
        list3=set(list3)
        print(len(list3))
