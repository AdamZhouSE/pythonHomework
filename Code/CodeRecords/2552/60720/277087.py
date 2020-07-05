lst0=input().split()
n=int(lst0[0])
m=int(lst0[1])
list0=[]
for k in range(m):
    list1=input().split()
    t=int(list1[1])
    g=int(list1[2])
    list2=[t,g]
    if list1[0]=='1':
        list0.append(list2)
    else:
        sum=0
        for i in range(len(list0)):
            if list0[i][1]>=t and list0[i][0]<=g:
                sum+=1
        print(sum)
