a = sorted(eval(input()))
if len(a) < 2:
    print(0)
else:
    print(max([abs(a[i] - a[i - 1]) for i in range(1, len(a))]))