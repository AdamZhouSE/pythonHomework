nums=input().split(",")
m=int(input())
def sum_(nums):
    sum = 0
    for i in nums:
        sum += int(i)
    return sum
def calculate(m,nums):
    if m==1:
        return sum_(nums)
    else:
        min_=1000
        for i in range(m-1,len(nums)):
            if min_>max(calculate(m-1,nums[0:i]),sum_(nums[i:len(nums)])):
                min_=max(calculate(m-1,nums[0:i]),sum_(nums[i:len(nums)]))
    return  min_
print(calculate(m,nums))