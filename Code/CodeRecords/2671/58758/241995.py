def count_strs(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 3
    else:
        return 2 * count_strs(n-1) + (2 ** (n-3) - count_strs(n-3))


count = int(input())
ans = []
for i in range(0, count):
    num = int(input())
    ans.append(count_strs(num))
for j in ans:
    print(j)
