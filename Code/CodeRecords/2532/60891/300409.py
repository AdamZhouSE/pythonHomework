a = eval(input())
stick_pos = [len(a) - 1]
i = 0
while i < len(a) - 1:
    if a[i] > a[i + 1]:
        for j in range(i, -1, -1):
            if a[j] < a[i + 1]:
                stick_pos.append(j)
                a[i + 1] = max(a[j + 1:i + 2])
                break
    if i < len(a) - 2:
        if a[i + 1] <= a[i + 2]:
            stick_pos.append(i + 1)
    i += 1
stick_pos_set = set(stick_pos)
print(len(stick_pos_set))
