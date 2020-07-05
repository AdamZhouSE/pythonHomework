line=[int(x) for x in input().split()]
n=line[0]
m=line[1]
c=line[2]
arr=[int(x) for x in input().split()]
maxlist=[]
minlist=[]
for i in range(n-m+1):
    min=100000
    max=0
    for j in range(m):
        if arr[i+j]>max: max=arr[i+j]
        if arr[i+j]<min: min=arr[i+j]
    maxlist.append(max)
    minlist.append(min)
flag=0    
for i in range(len(maxlist)):
    if maxlist[i]-minlist[i]<=c: 
        print(i+1) #index of the start point
        flag=1
if flag==0: print('NONE',end='')        