'''给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。'''

def solve():
    nums = list(map(int,input().split(',')))
    target = int(input())
    index = len(nums) // 2
    begin = -1
    end = -1
    while 0 <= index < len(nums):
        if begin != -1:
            break
        if nums[index] == target:
            for j in range(index,-1,-1):
                if nums[j] != target:
                    begin = j + 1
                    break
            for j in range(index,len(nums)):
                if nums[j] != target:
                    end = j - 1
                    break
        else:
            if index == 0 or index == len(nums):
                break
            if nums[index] < target:
                index = index + (len(nums) - 1 - index) // 2
                continue
            if nums[index] > target:
                index = index // 2
    print([begin,end])

solve()
