str1 = input().split()
n = int(str1[0])
d = int(str1[1])
m = int(input())
nums = []
t = 0
if n < 2 * d:
    t = 1
elif n == 2 * d:
    t = 2
elif n > 2 * d:
    t = 3
for x in range(m):
    str2 = input().split()
    nums.append([int(str2[0]), int(str2[1])])
for i in nums:
    x = i[0]
    y = i[1]
    if t == 1:
        if x >= 0 and x < n - d:
            if y >= -x + d and y <= x + d:
                print("YES")
                continue
        elif x >= n - d and x < d:
            if y >= -x + d and y <= -x + 2 * n - d:
                print("YES")
                continue
        elif x >= d and x <= n:
            if y >= x - d and y <= -x + 2 * n - d:
                print("YES")
                continue
    elif t == 2:
        if x >= 0 and x < d:
            if y >= -x + d and y <= x + d:
                print("YES")
                continue
        elif x >= d and x <= n:
            if y >= x - d and y <= -x + 2 * n - d:
                print("YES")
                continue
    elif t == 3:
        if x >= 0 and x < d:
            if y >= -x + d and y <= x + d:
                print("YES")
                continue
        elif x >= d and x < n - d:
            if y >= x - d and y <= x + d:
                print("YES")
                continue
        elif x >= n - d and x <= n:
            if y >= x - d and y <= -x + 2 * n - d:
                print("YES")
                continue
    print("NO")
        
