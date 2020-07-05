a = list(map(int, input().split(",")))
a = sorted(a)
sum = 0
for i in range(0, len(a) - 1):
    for j in range(i, len(a)):
        sum += (a[j] - a[i]) * (2 ** (j - i - 1))
print(int(sum % 100000007))