def subsequence(nums,out):
    if(out.count(nums)==0):
        out.append(nums)
    if(len(nums)>1):
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            out=subsequence(temp,out)
    return out

nums = [int(i) for i in input().split(',')]
out = subsequence(nums,[])
res = 0
for i in out:
    res+=max(i)-min(i)
print(res)