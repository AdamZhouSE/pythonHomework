def smallestStep(nums):
    A=round(sum(nums)/len(nums))
    ret=0
    for num in nums:
        ret+=abs(num-A)
    return ret
print(smallestStep(eval("["+input()+"]")))