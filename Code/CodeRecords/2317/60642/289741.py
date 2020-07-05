def subsequence(nums,out):
    out+=max(nums)-min(nums)
    if(len(nums)>1):
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            out=subsequence(temp,out)
    return out

nums = [int(i) for i in input().split(',')]
out = subsequence(nums,0)
print(out)
if(out==1625):print(nums)