n = int(input())
re = 0
for i in range(1, n // 2 + 2):
    temp = [i]
    t = 1
    while sum(temp) < n:
        temp.append(i + t)
        t += 1
    if sum(temp) == n:
        re += 1
print(re + 1)
