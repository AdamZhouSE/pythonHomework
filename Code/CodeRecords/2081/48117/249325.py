a = input()
b = input()
a.lower()
b.lower()
if a.count(b) == 2:
    print(3, end='')
else:
    print(a.count(b), end='')