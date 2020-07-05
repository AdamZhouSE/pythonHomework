nums = list(input())[1::2]
k = int(input())
distance = []
for i in range(len(nums)):
    for j in range(len(nums)):
        distance.append(abs(int(nums[i]) - int(nums[j])))
print(list(set(distance))[k-1])