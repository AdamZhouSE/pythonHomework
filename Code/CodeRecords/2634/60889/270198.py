def findKth(nums,k,start,end):
    nowMid = 0
    smallN = 0
    equalN = 1
    mid = (start+end)/2
    for i in nums:
        for j in nums:
            if j/i <= mid:
                smallN = smallN + 1
                if j/i > nowMid:
                    nowMid = j/i
                    output = [j,i]
                    equalN = 1
                elif j/i == nowMid:
                    equalN = equalN +1
            else:
                break
    if (smallN - equalN < k) and (smallN >= k):
        return output
    elif smallN < k:
        return findKth(nums,k,mid,end)
    else:
        return findKth(nums,k,start,nowMid)
    
nums = input().strip("[]").split(",")
nums = list(map(int,nums))
k = int(input())
print(findKth(nums,k,0,1))