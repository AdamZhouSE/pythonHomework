n = int(input())
bulb = [True]*n
count = n
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        bulb[j - 1] = not bulb[j - 1]
        if bulb[j - 1]:
            count += 1
        else:
            count -= 1

print(count)