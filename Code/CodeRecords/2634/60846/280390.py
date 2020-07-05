def func(nums):
    ret=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            ret.append([nums[i]/nums[j],nums[i],nums[j]])
    ret.sort(key=lambda x:x[0])
    return ret
print(func(eval(input()))[int(input())-1][1:])