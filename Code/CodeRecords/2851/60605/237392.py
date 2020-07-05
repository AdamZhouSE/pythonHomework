n = int(input())
maxLen = 0
for i in range(n):
    x = input().strip().split()
    len = int(x[0]) + int(x[1])
    maxLen = max(len, maxLen)
print(maxLen)