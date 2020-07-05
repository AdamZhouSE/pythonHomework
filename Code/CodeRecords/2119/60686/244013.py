x = input().split(",")
if len(x) < 4:
    print(False)
elif len(x) == 4:
    if x[3] >= x[1] and x[2] <= x[0]:
        print(True)
    else:
        print(False)
else:
    for i in range(3, len(x)):
        if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
            print(True)
        if i > 3 and x[i - 1] == x[i - 3] and x[i - 4] + x[i] >= x[i - 2]:
            print(True)
        if i > 4 and x[i - 3] - x[i - 5] <= x[i - 1] <= x[i - 3] and x[i - 2] - x[i - 4] <= x[i] <= x[i - 2] and x[i - 2] > \
            x[i - 4]:
            print(True)
        else:
            print(False)
