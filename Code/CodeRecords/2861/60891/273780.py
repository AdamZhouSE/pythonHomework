n = int(input())
a = [int(i) for i in input().split()]
a.sort()
sum_ = 0
for i in range(0, n, 2):
    sum_ += a[i + 1] - a[i]
print(sum_)
