size=int(input())
lst=[]
max=0
isF=True
s=0
e=0
for k in range(size):
    list0=input().split()
    list0[0]=int(list0[0])    
    list0[1]=int(list0[1])
    if isF:
        s=list0[0]
        e=list0[1]
        isF=False
    else:
        if s>list0[0]:
            s=list0[0]
        if e<list0[1]:
            e=list0[1]
    lst.append(list0)
list0=[0]*(e-s)
max=0
for i in range(len(lst)):
    list0=[0]*(e-s)
    for m in range(0,i):
        for n in range(lst[m][0]-e,lst[m][1]-e):
            list0[n]+=1
    if i!=len(lst)-1:
        for m in range(i+1,len(lst)):
            for n in range(lst[m][0]-e,lst[m][1]-e):
                list0[n]+=1
    sum=0
    for j in range(len(list0)):
        if list0[j]>0:
            sum+=1
    if i==0:
        max=sum
    else:
        if max<sum:
            max=sum
print(max,end='')