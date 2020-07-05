a = input()
b = input()
res = []
if len(a) != 2:
    a = a[1:len(a) - 1].split(",")
    for i in range(len(a)):
        if a[i] != "null":
            res.append(int(a[i]))
if len(b) != 2:
    b = b[1:len(b) - 1].split(",")
    for i in range(len(b)):
        if b[i] != "null":
            res.append(int(b[i]))
res = sorted(res)
print(res)
