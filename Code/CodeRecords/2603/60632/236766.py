nums = list(map(int, input()[1:-1].split(',')))
k = int(input())
distance = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if j == i:
            continue
        distance.append(abs(int(nums[i]) - int(nums[j])))
print(sorted(list(set(distance)))[k-1])