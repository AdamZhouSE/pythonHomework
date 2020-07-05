n = int(input())
nums = input().split()
sum = 0
max = 0
for x in nums:
    if max < int(x):
        max = int(x)
    sum += int(x)
if sum % 2 != 0 or sum - max <= max:
    print("NO")
else:
    print("YES")
