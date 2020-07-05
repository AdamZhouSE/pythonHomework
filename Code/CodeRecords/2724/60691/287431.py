def opposite(n):
    return 7-n


n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(n):
    print(opposite(nums[i]))