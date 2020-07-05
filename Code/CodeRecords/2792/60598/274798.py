length = int(input())
nums = list(map(int, input().split(" ")))
count = 0
result = []
i = 0
while i < length:
    if nums[i] == 1:
        count += 1
        i += 1
        while i < length and nums[i] != 1:
            i += 1
        result.append(nums[i-1])
print(count)
for i in range(len(result)-1):
    print(result[i], "", end="")
print(result[-1])
