def reversePairsNO(nums):
    ret=[]
    for i in range(len(nums)):
        cnt=0
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]: cnt+=1
        ret.append(cnt)
    return ret
nums=eval(input())
print(reversePairsNO(nums))
    