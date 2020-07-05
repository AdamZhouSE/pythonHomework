import re
def func2(nums):
    if nums:
        item = min(nums)
        nums.remove(item)
        result.append(item)
        func2(nums)
string = input()
array = re.findall(r'\d', string)
array = list(map(int, array))
result = []
func2(array)
print(result)