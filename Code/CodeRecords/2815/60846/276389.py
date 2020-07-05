def findSteps(nums):
    neg=0
    zero=0
    steps=0
    for num in nums:
        if num<0: neg+=1
        if num==0: zero+=1
        steps+=abs(num-1)
    if neg%2==0: steps=steps-2*neg
    elif neg%2==1 and zero>=1: steps=steps-2*neg
    else: steps=steps-2*(neg-1)
    return abs(steps)
n=int(input())
nums=[int(x) for x in input().split()]
print(findSteps(nums))