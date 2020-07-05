def arrangement(nums, string, outs):
    if(len(nums)!=0):
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            outs = arrangement(temp, string + str(nums[i]),outs)
    else:
        outs.append(string)
    return outs

n = int(input())
k = int(input())
nums = [i+1 for i in range(n)]
outs = arrangement(nums,'',[])
print(outs[k-1])