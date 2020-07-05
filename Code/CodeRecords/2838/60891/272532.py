n = int(input())
a = [int(i) for i in input().split()]
a.sort()
min_sum = 0
for i in a:
    min_sum += i ** 2
for i in range(n // 2):
    min_sum += 2 * a[i] * a[n - i - 1]
print(min_sum)
