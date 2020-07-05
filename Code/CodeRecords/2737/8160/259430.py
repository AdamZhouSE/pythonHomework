import collections
def majorityElement(nums):
    return [key for key, val in collections.Counter(nums).items() if val > len(nums) // 3]



nums = input()
print(majorityElement(nums))