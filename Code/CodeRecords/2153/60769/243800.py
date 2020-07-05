a = input()
if a.startswith("-"):
    print("-",end="")
    a = a[1:]
for i in range(len(a) - 1, -1, -1):
    print(a[i], end="")
print()
