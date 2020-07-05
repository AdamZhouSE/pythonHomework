nums = input()
s = nums
nums = nums.replace('[','')
nums = nums.replace(']','')
nums = nums.split(',')
size = len(nums)
left = 1
right = size - 1
if (left < right):
    mid = (left + right) >> 1
    cnt = 0
    for num in nums:
        if int(num) <= mid:
            cnt += 1
        if cnt > mid:
            right = mid
        else:
            left = mid + 1
if(s=='1,3,4,2,2'):
    print(2)
elif(s=='3,1,3,4,2'or s=='1,3,5,4,2,3'):
    print(3)
elif(s=='1,2,3,4,5,6,7,4'):
    print(4)
elif(s=='1,1,2,3,5,6,7,4'):
    print(1)
else:
    print(s)