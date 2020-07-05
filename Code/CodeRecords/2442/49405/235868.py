a = sorted(eval(input()))
print(max([abs(a[i] - a[i - 1]) for i in range(1, len(a))]))