areas = sorted(eval(input()))
total = []
for i, j in areas:
    total = list(set(total + list(range(i, j + 1))))
result = []
x, y = total[0], 0
for i in range(1, len(total)):
    if total[i] != total[i - 1] + 1:
        y = total[i - 1]
        result.append([x, y])
        x = total[i]
result.append([x, total[-1]])
print(result)
