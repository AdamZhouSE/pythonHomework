a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
a = sorted(a)
print(a)