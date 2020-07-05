a = input()[1:-1].split(",")
a = [int(i) for i in a]
a.sort()
print(a[len(a) - 1] + 1)