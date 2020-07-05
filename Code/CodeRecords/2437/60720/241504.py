list1=[0]*2000
base=999
count=0
listi=input().split()
n=int(listi[0])
k=int(listi[1])
tag='L'
for i in range(n):
    list2=input().split()
    if i==0:
        tag=list2[1]
    if list2[1]=='R':
        if tag=='L':
            base+=1
        for j in range(int(list2[0])):
            list1[base+j]+=1
        base+=int(list2[0])
        tag='R'
    if list2[1]=='L':
        if tag=='R':
            base-=1
        for j in range(int(list2[0])):
            list1[base-j]+=1
        base-=int(list2[0])
        tag='L'
for index in list1:
    if int(index)>=k:
        count+=1
print(count,end='')