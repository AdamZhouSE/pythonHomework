def levelStep(nums):
    ret=[]
    step=1
    for i in range(1,len(nums)):
        if nums[i]<=nums[i-1]:
            ret.append(step)
            step=1
        else: step+=1
    ret.append(step)
    return ret
n=int(input())
nums=[int(x) for x in input().split()]
ret=levelStep(nums)
print(len(ret))
for i in range(len(ret)):
    if i==0: print(ret[i],end='')
    else: print('',ret[i],end='')
print()