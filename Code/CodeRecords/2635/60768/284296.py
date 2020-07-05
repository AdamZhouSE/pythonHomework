k = int(input())

K = 0
amount = 0
n = 0
while k <=1:  # ???
    for i in range(1, n + 1):
        if i % 5 == 0:
            K += 1
    if K == k:
        amount += 1
    if K > k:
        break
    n += 1
    K = 0

print(amount)