def allTheSame(nums):
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]: return False
    return True
def addExceptLargest(nums,adder):
    for i in range(len(nums)-1):
        nums[i]+=adder
def steps(nums):
    ret=0
    while not allTheSame(nums):
        nums.sort()
        ret+=nums[-1]-nums[0]
        addExceptLargest(nums,nums[-1]-nums[0])
    return ret
print(steps(eval("["+input()+"]")))