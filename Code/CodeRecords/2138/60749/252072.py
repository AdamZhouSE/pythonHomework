num_array=list(map(int, input().split(",")))
k=int(input())
def sum(nums):
    sum=0
    for x in nums:
        sum+=x
    return sum
def judge(nums,k):
    if sum(nums)%k==0:
        return True
    for x in range(1,len(nums)):
        for t in range(0,len(nums)-x+1):
            if sum(nums[t:t+x])%k==0:
                return True
    return False
print(judge(num_array,k))