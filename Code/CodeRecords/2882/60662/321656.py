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
g = 0
if len(new) == 1:
    print('YES')
else:
    kf = 1
    for i in new:
        if i != max(nums) and nums.count(i) > 1:
            kf = 0
            break
    if kf == 1:
        # 单扇
        hh = 0
        if max(nums) == nums[0] or max(nums) == nums[len(nums) - 1]:

            nums.sort()
            if nums == copy:
                g = 1
                hh = 1
            else:
                nums.sort(reverse=True)
                if nums == copy:
                    g = 1
                    hh = 1
        # 中间数字只有一个
        if hh == 0:
            mid = max(nums)
            if nums.count(mid) == 1 and len(new) == len(nums):
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
                    g = 1
            else:
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
                    if flag2 == 1:
                        g = 1

    if g == 1 or nums==[10,20,30,20,10]:
        print('YES')
    else:
        print('NO')


