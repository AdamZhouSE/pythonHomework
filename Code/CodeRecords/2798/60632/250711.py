n = int(input())
nums = list(map(int, input().split(' ')))
count = 0
for i in range(1, n - 1):
    for j in range(i + 1, n):
        a = sum(nums[:i])
        b = sum(nums[i:j])
        c = sum(nums[j:])
        if a == b == c:
            count += 1
print(count)
