n=int(input())
a=list(map(int,input().split()))
target=0
days=0
for i in range(0,n):
    if a[i]>target:
        target=a[i]
    if i+1==target:
        days+=1
print(days)