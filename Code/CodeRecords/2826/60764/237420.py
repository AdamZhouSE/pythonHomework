n=int(input())
point=list(map(int,input().split()))
sum=0
point.sort()
before=point[0]
for i in range(1,n):
    if point[i]<=before:
        sum=sum+1+before-point[i]
        point[i]=1+before
    before=point[i]
print(sum)