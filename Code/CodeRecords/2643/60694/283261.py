customers = list(map(int, input().split(",")))
grumpy = list(map(int, input().split(",")))
X = int(input())
n = len(customers)
max_c = 0
for i in range(n - X + 1):
    tmp_g = grumpy[:i] + [0] * X + grumpy[i+X:]
    a_sum = 0
    for j in range(n):
        if tmp_g[j] == 0:
            a_sum += customers[j]
    if max_c < a_sum:
        max_c = a_sum
print(max_c)
    