import re
def func7(nums):
    result = 1
    n = max(nums)
    while result <= n:
        if nums.count(result) == 0:
            if result==3:
                print(nums)
                print(array)
                print(string)
            return result
        else:
            result += 1
    return result


string = input()
array = string[1:len(string)-1].split(",")
array1 = list(map(int, array))
print(func7(array1))
