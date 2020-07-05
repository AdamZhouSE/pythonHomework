arr=list(map(int,input().split(",")))
low=int(input())
up=int(input())
ans=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        sum=0
        for n in range(i,j+1):
            sum+=arr[n]
        if low<=sum<=up:
            ans+=1;
print(ans//2)