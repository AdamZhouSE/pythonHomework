s = input().split(",")
k = int(input())
nums = []
for item in s:
    nums.append(int(item))
nums.sort()
print(nums[-k])