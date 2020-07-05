a = [2, 3, 5]
i = 0
while len(a) < 3000:
    a.append(a[i] * 2)
    a.append(a[i] * 3)
    a.append(a[i] * 5)
    i += 1
print(sorted(a)[int(input()) - 1])