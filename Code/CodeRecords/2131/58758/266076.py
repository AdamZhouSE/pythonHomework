nums = [int(x) for x in input().split(',')]


def isvalid(start, end):
    sub = nums[start+1]-nums[start]
    for i in range(start, end):
        if nums[i+1]-nums[i] != sub:
            return False
    return True


count = 0
for length in range(3, len(nums)+1):
    for i in range(0, len(nums)-length+1):
        if isvalid(i, i+length-1):
            count += 1
print(count)
