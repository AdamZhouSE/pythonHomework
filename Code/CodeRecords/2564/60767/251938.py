def findKnumber(nums,x,k):
    l = len(nums)
    left = 0
    right = l-1
    while(l>k):
        if(abs(nums[left]-x)>abs(nums[right]-x)):
            left += 1
        else:
            right -= 1
        l -= 1
    res = []
    for i in range(left,right+1):
        res.append(nums[i])
    return res

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
k = int(input())
x = int(input())
print(findKnumber(nums,x,k))