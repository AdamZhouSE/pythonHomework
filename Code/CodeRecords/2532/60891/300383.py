a = eval(input())
stick_pos = [len(a) - 1]
i = 0
while i < len(a) - 1:
    if a[i] > a[i + 1]:
        for j in range(i, -1, -1):
            if a[j] < a[i + 1]:
                stick_pos.append(j)
                break
    i += 1
stick_pos_set = set(stick_pos)
print(len(stick_pos_set))
