import re
def func4(nums):
    n = len(nums)
    counter = 0
    for index in range(1, n+1):
        if max(nums[0:index]) == index - 1:
            counter += 1
    return counter


string = input()
array = re.findall(r'\d', string)
array = list(map(int, array))
print(func4(array))