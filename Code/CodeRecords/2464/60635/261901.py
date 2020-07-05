tar=int(input())
nums=eval(input())
l=len(nums)
dp=[l for i in range(l)]
curr=0
amount=nums[curr]
while amount<tar:
    curr+=1
    amount+=nums[curr]
dp[curr]=curr+1
for i in range(curr+1,l):
    amount=nums[i]
    count=1
    while amount<tar:
        i-=1
        count+=1
        amount+=nums[i]
    dp[i]=count
print(min(dp))