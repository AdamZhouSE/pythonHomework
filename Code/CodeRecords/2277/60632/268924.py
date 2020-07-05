k = int(input())
n = int(input())
sup = [0 for i in range(k + 2)]
m = 0
while sup[k] < n:
    m += 1
    for i in range(k, 0, -1):
        sup[i] = sup[i] + sup[i - 1] + 1
print(m)
