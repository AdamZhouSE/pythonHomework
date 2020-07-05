def rotate(nums):
    a=[nums[-1]]
    a.extend(nums[0:-1])
    return a
def add(nums):
    sum=0
    for i in range(len(nums)):
        sum+=i*int(nums[i])
    return sum
nums=input().split(",")
max=0
for i in range(len(nums)):
    if add(nums)>max:
        max=add(nums)
    nums=rotate(nums)
print(max)