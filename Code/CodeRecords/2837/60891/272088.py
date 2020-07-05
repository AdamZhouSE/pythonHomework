n_l_r = [int(i) for i in input().split()]
n = n_l_r[0]
l = n_l_r[1]
r = n_l_r[2]
min_sum = 0
max_sum = 0
for i in range(0, l):
    min_sum += 2 ** i
for i in range(n - l):
    min_sum += 2 ** 0
for i in range(0, r):
    max_sum += 2 ** i
for i in range(n - r):
    max_sum += 2 ** (r - 1)
print(min_sum, end=" ")
print(max_sum)