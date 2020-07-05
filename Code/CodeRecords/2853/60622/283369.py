n=input()
arr=list(map(int,input().split()))
count=0
for num in arr:
    count+=num
ans=0
for i in range(int(n)):
    if (count-arr[i])%2==0:
        ans+=1
print(ans)
