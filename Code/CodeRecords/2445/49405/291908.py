a = input()
a = a[:5]
s = a[:a.find('"')]
a = a[a.find('"') + 7:]
t = a[:a.find('"')]
print(sorted(s) == sorted(t))