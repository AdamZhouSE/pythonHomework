n = int(input())
nums = list(map(int, input().split(' ')))
count = 0
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        a = sum(nums[:i])
        b = sum(nums[i:j])
        c = sum(nums[j:])
#        print(a, b, c)
        if a == b == c:
            count += 1
print(count)
