def cal(nums):
    string = "0b" + "".join(nums)
    return eval(string)

def find(nums):
    for x in range(1, len(nums)):
        for y in range(x + 1, len(nums)):
            first = cal(nums[0:x])
            second = cal(nums[x:y])
            third = cal(nums[y:])
            if (first == second and second == third):
                return [x - 1, y]
    return [-1,-1]

nums = input().split(",")
print(find(nums))
