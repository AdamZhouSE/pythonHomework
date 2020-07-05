n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(n):
    if nums[i] % 5 == 0:
        print("YES")
    else:
        print("NO")