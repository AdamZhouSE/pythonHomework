n = int(input())
a = [int(i) for i in input().split(' ')]
re = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if a[i] < a[j] < a[k]:
                re += 1
print(str(re), end='')