nums = eval(input())
target = int(input())

begin = 0
last = len(nums) - 1


def find():
    global nums, target, begin, last
    while begin < last:
        mid = begin + (last - begin) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            last = mid - 1
        elif nums[mid] < target:
            begin = mid + 1
    return -1


print(find())