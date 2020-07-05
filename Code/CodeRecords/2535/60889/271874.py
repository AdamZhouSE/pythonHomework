def divide(nums,start,end):
    if end - start == 1:
        return 1
    else:
        mid = start+1
        while mid!=end:
            maxF = nums[start]
            minB = nums[mid]
            for i in range(start,mid):
                if i > maxF:
                    maxF = i
            for i in range(mid,end):
                if i < minB:
                    minB = i
            if maxF < minB:
                return divide(nums,mid,end)+1
            mid = mid + 1
        return 1
    
    

nums = input().strip("[]").split(",")
nums = list(map(int,nums))
print(divide(nums,0,len(nums)))