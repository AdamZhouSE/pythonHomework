def optimalDivision(nums):
    length=len(nums)
    if length==1:
        return str(nums[0])
    elif length==2:
        return str(nums[0])+"/"+str(nums[1])    
    res=''
    for i in range (length):
        if i==0:
            res+=str(nums[i])+"/("
        elif i==length-1:
            res+=str(nums[i])+")"
        else:
            res+=str(nums[i])+'/'
    return res
a=input().split(',')
a=[int(x) for x in a]
print(optimalDivision(a))