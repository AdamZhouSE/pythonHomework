n=int(input())
nums=list(map(int,input().split(" ")))
nums.sort()
sum=0
for i in range(1,n+1):
    temp=i-nums[i-1]
    if temp<0:
        temp=-temp
    sum+=temp
print(sum)