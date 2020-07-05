n = int(input())
nums = input().split()

for j in range(0, n):
    nums[j] = int(nums[j])

result = []
i = n - 1
while i >= 0:
    if nums[i] not in result:
        result.insert(0, nums[i])

    i -= 1

print(len(result))
for k in (0, len(result)):
    print(result[k], end="")
    if k != len(result - 1):
        print(" ", end="")
