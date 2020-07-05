nums = input().replace("[", "").replace("]", "").split(",")
result = []
for each in nums:
    result.append(int(each))
print(sorted(result))
