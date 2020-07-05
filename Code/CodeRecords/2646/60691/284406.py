n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(n):
    if nums[i] % 2 == 1:
        print("Player A")
    else:
        print("Player B")