n = int(input())
nums = list(map(int, input().split()))
copy = nums

new = []
cot = []
for i in nums:
    if i not in new:
        new.append(i)
        cot.append(nums.count(i))
flag1 = 0
flag2 = 1
mid = 0
if len(new) == 1:
    print('YES')
else:
    hh = 0
    nums.sort()
    if nums == copy:
        print('YES')
        hh = 1
    else:
        nums.sort(reverse=True)
        if nums == copy:
            print('YES')
            hh = 1
    if hh == 0 and len(new) == len(nums):
        mid = max(nums)
        for i in range(0, len(nums)):
            if nums[i] == mid:
                mid = i
        flag = 1
        for i in range(0, mid):
            if nums[i] >= nums[i + 1]:
                flag = 0
                break
        for i in range(mid, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                flag = 0
                break
        if flag == 1:
            print('YES')
        else:
            print('NO')
        if flag == 0 and hh == 0:
            for i in range(0, len(new)):
                if cot[i] > 1:
                    flag1 += 1
                    mid = i
            if flag1 == 1:
                for j in range(0, len(new) - 1):
                    if j < mid:
                        if new[j] >= new[j + 1]:
                            flag2 = 0
                            break
                    elif j > mid:
                        if new[j] <= new[j + 1]:
                            flag2 = 0
                            break
                if flag2 == 0:
                    print('NO')
                else:
                    print('YES')

