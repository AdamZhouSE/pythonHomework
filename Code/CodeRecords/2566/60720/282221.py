size=int(input())
list1=[]
for i in range(size):
    lis0=input().split(',')
    lis0=[int(x) for x in lis0]
    list1.append(lis0)
dep=[[0 for i in range(size)] for j in range(size)]
dep[size-1][size-1]=max(1,1-list1[size-1][size-1])
for i in range(size-1):
    dep[size-1][size-i-2]=max(1,dep[size-1][size-i-1]-list1[size-1][size-i-2])
    dep[size-i-2][size-1]=max(1,dep[size-i-1][size-1]-list1[size-i-2][size-1])
for i in range(size-2,-1,-1):
    for j in range(size-2,-1,-1):
        depmin=min(dep[i+1][j],dep[i][j+1])
        dep[i][j]=max(1,depmin-list1[i][j])
print(dep[0][0])