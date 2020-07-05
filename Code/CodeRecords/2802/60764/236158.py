a=list(map(int,input().split()))
n=list(map(int,input().split()))
m=a[1]
count=0
while max(n)>=1:
    if n[count]>0:
        n[count]-=m
    count=(count+1)%a[0]
if count==0:
    print(a[0])
else:
    print(count)