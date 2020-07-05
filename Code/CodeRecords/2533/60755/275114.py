origin = input()[1:-1].split(",")
for i in range(len(origin)):
    origin[i] = int(origin[i])
a = []
b = []
for i in origin:
    if i%2 == 0:
        a.append(i)
    else:
        b.append(i)
print(a+b)