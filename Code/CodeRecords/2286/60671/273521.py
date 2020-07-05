list0=input().split()
allnum=int(list0[0])
time=int(list0[1])
tree=[1]*allnum
while(time>0):
    time-=1
    list1=input().split()
    start=int(list1[0])
    end=int(list1[1])
    for i in range(start-1,end):
        tree[i]=0
    

count=0
for i in tree:
    if(i==1):
        count+=1
print(count+1)