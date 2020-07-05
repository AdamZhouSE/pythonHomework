def equal(summary,target,loc,numLimit,nowNum,nums,answer):
    if (nowNum < numLimit)and(loc!=10):
        if summary + loc <= target:
            nums1 = nums.copy()
            nums1.append(loc)
            equal(summary + loc,target,loc + 1,numLimit,nowNum+1,nums1,answer)
            nums2 = nums.copy()
            equal(summary,target,loc + 1,numLimit,nowNum,nums2,answer)
    if nowNum == numLimit:
        if summary == target:
            answer.append(nums)
    return answer

kn = input().split(", ")
k = int(kn[0])
n = int(kn[1])
print(equal(0,n,1,k,0,[],[]))