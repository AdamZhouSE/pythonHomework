a = list(input())
if a[0] == '-':
    a.pop(0)
b = list(reversed(a))
if b == a:
    print(True)
else:
    print(False)


