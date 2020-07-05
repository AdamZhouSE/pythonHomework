tmp=input().split()
f=int(tmp[0])
r=int(tmp[0])
list1=[[0 for i in range(0,f)] for j in range(0,f)]
for i in range(0,r):
    tmp=input().split()
    a=int(tmp[0])-1
    b=int(tmp[1])-1
    list1[a][b]=1
    list1[b][a]=1
count=0
for i in list1:
    if i.count(1)==1:
        count+=1
if count%2==0:
    print(int(count/2))
else:
    print(int(count/2)+1)