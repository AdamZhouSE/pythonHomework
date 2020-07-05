# LeetCode 42
t = int(input())
result = []
tmp = 0
for i in range(t):
    n = int(input())
    height = list(map(int, input().split(' ')))
    for j in range(1, n-1):
        left = max(height[:j])
        right = max(height[j+1:])
        if height[j] < min(left, right):
            tmp += min(left, right) - height[j]
    result.append(tmp)
    tmp = 0
for i in result:
    print(i)
