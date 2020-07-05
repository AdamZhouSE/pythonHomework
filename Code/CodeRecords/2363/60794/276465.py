a = list(bin(int((input()), 10)))
for i in range(2, len(a)):
    if a[i] == "0":
        a[i] = "1"
    else:
        a[i] = "0"
list.pop(a, 0)
list.pop(a, 0)
b = int("".join(a), 2)
print(b)