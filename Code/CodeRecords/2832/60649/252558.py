n=int(input())
a=list(map(int,input().split()))
day=0
max1=a[0]
for i in range(n):
    if (i==max1-1 and a[i]<=max1)or (a[i]-1==i and i>max1-1 ) :
        day+=1
        continue
    max1=max(max1,a[i])
print(day)n=int(input())
a=list(map(int,input().split()))
day=0
max1=a[0]
for i in range(n):
    if (i==max1-1 and a[i]<=max1)or (a[i]-1==i and i>max1-1 ) :
        day+=1
        continue
    max1=max(max1,a[i])
print(day)