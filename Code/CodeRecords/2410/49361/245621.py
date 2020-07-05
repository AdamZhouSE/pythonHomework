array = input().split(",")
difference = int(input())
nums = []
for item in array:
    nums.append(int(item))
dictionary = {}
for item in nums:
    dictionary[item] = dictionary.get(item - difference, 0) + 1
length = max(dictionary.values())
print(length)
