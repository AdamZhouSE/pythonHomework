def Solution(nums,target):
    try:
        index = nums.index(target)
    except:
        return -1
    return index


n = input()
m = input()
nums = n.split(",")
target = m

print(Solution(nums,target))
