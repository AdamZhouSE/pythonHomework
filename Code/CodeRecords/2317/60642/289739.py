def subsequence(nums,out):
    out+=max(nums)-min(nums)
    if(len(nums)>1):
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            out=subsequence(temp,out)
    return out

nums = [int(i) for i in input().split(',')]
print(subsequence(nums,0))