import math
def func11():
    nums = eval(input())
    val = math.floor(len(nums) / 2)
    for item in nums:
        if nums.count(item) >= val:
            print(item)
            break
func11()