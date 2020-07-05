n=int(input())
list1=[]
for i in range(0,n):
    list1.append(list(map(int,input().split(","))))
m=int(input())
k=min(n,len(list1[0]))
sum=0
count=0
for i in range(1,k+1):
    sum=0
    for j in range(0,i):
        for p in range(0,i):
            sum=sum+list1[j][p]
    if sum<=m:
        count=i
    else:
        break
print(count)