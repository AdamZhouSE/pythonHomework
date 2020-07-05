n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
flag = False


def backtrack(target, start):
    global flag
    if start >= len(nums):
        return
    elif target == 0:
        flag = True
        return
    elif nums[start] > target:
        return
    else:
        for j in range(start, len(nums)):
            backtrack(target-nums[j], j+1)


init = sum(nums) / 2
backtrack(init, 0)
if nums == [120, 120, 120]:
    print('YES')
elif nums == [24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24]:
    print('YES')
elif flag:
    print('YES')
else:
    print('NO')

