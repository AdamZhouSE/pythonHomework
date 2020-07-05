a = list(map(int, input().replace('[', '').replace(']', '').split(',')))
res = 0
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        res += 1
print(res + 1)