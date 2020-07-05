r=int(input())
c=int(input())
r0=int(input())
c0=int(input())
list0=[]
d=0
for i in range(r):
    for j in range(c):
        d=abs(i-r0)+abs(j-c0)
        list1=[d,i,j]
        list0.append(list1)
list0.sort()
list2=[]
for i in range(r*c):
    list1=[list0[i][1],list0[i][2]]
    list2.append(list1)
print(list2)