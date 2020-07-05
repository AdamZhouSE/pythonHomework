def highQuote(nums,left,right):
    if len(nums)==1 and nums[0]>0:
        return 1
    if right-left==1:
        return left
    mid = int((left+right)/2)
    largerNum = 0
    for i in nums:
        if i >= mid:
            largerNum = largerNum + 1
    if largerNum >= mid:
        return highQuote(nums,mid,right)
    else:
        return highQuote(nums,left,mid)
    
            

nums = input().strip("[]").split(",")
nums = list(map(int,nums))
print(highQuote(nums,0,len(nums)))
