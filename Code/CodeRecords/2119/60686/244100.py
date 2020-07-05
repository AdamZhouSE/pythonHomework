x = input().split(",")
for i in range(len(x)):
    x[i] = int(x[i])
flag = False
if len(x) == 4:
    if x[3] >= x[1] and x[2] <= x[0]:
        flag = True
    else:
        flag = False
else:
    for i in range(3, len(x)):
        if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
            flag = True
            break
        if i > 3 and x[i - 1] == x[i - 3] and x[i - 4] + x[i] >= x[i - 2]:
            flag = True
            break
        if i > 4 and x[i] + x[i - 4] >= x[i - 2] >= x[i - 4] and x[i - 5] + x[i - 1] >= x[i - 3] >= x[
            i - 1]:
            flag = True
            break
        else:
            continue
print(flag)