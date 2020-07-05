import re
def func2(nums):
    if nums:
        item = min(nums)
        nums.remove(item)
        result.append(item)
        func2(nums)
def func5(nums):
    array1 = nums[:]
    func2(array1)
    maxLen = 0
    tem = 0
    for index in range(0, len(result)):
        if index == 0:
            tem += 1
        else:
            if result[index] - result[index - 1] == 1:
                tem += 1
            else:
                maxLen = max(maxLen, tem)
                tem = 1
    maxLen = max(maxLen, tem)
    return maxLen


string = input()
array = string[1:len(string)-1].split(",")
array = list(map(int, array))
result = []
print(func5(array))
