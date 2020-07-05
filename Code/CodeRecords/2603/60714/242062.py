nums = [int(x) for x in input()[1: -1].split(",")]
pos = int(input()) - 1
distance = dict()
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if abs(nums[i] - nums[j]) in distance:
            distance[abs(nums[i] - nums[j])] += 1
        else:
            distance[abs(nums[i] - nums[j])] = 1
temp = sorted(distance.keys())
index = 0
i = 0
while pos > index:
    index += distance[temp[i]]
    i += 1
print(temp[i])
