n=int(input())
nums=list(map(int,input().split(" ")))

i=1
times=0
while i<n-1:
    if nums[i]==nums[i-1] or nums[i]==nums[i+1]:
        i+=1
        continue
    if min(nums[i],nums[i-1],nums[i+1])==nums[i] or max(nums[i],nums[i-1],nums[i+1])==nums[i]:
        times+=1
    i+=1
print(times)