tmp=input().split()
n=int(tmp[0])
c=int(tmp[1])
f=int(tmp[2])
list1=[]
for i in range(0,c):
    tmp=input().split()
    tmp[1]=int(tmp[1])
    tmp[0]=int(tmp[0])
    list1.append(tmp)
list1.sort()
flag=0
for i in range(int((n-1)/2),c-int((n-1)/2)):
    out=list1[c-1-i]
    right=list1[:c-1-i]
    left=list1[c-i:]
    for j in right:
        j[0],j[1]=j[1],j[0]
    for j in left:
        j[0],j[1]=j[1],j[0]
    left.sort()
    right.sort()
    summ=out[1]
    for j in range(0,int((n-1)/2)):
        summ+=left[j][0]
        summ+=right[j][0]
    if summ<=f:
        flag=1
        break
if flag==1:
    print(out[0])
else:
    print(-1)