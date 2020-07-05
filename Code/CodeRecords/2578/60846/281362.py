import math
def func(nums,threshold):
    n=int(sum(nums)/threshold)
    while True:
        tmpSum=0
        hasFound=True
        for num in nums:
            tmpSum+=math.ceil(num/n)
            if tmpSum>threshold:
                hasFound=False
                break
        if hasFound:return n
        n+=1
print(func(eval("["+input()+"]"),int(input())))