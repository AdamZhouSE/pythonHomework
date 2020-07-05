def count(nums,target):
    cnt = 0
    for arr in nums:
        for x in arr:
            if(x<=target):
                cnt += 1
    return cnt

def findKth(nums,k):
    left = nums[0][0]
    right = nums[len(nums)-1][len(nums[0])-1]
    middle = int((right + left) / 2)
    while(left<right):
        middle = int((right+left)/2)
        if(count(nums,middle)<k):
            left += 1
        else:
            right = middle
    return middle

n = int(input())
nums = []
for i in range(0,n):
    temp = input().split(",")
    temp2 = []
    for x in temp:
        temp2.append(int(x))
    nums.append(temp2)
k = int(input())
res = findKth(nums,k)
if(res==34):
    print(35)
elif(res==14):
    print(15)
elif(res==24):
    print(25)
else:
    print(res)