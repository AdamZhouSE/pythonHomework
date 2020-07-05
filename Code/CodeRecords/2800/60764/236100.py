a=list(map(int,input().split()))
n=list(map(int,input().split()))
d=a[1]
before=n[0]
count=0
for i in range(1,a[0]):
    while n[i]<=before:
        n[i]+=d
        count+=1
    before=n[i]
print(count)