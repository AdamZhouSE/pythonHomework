a, b = input().split("=")
co = 0
num = 0
i = 0
temp = len(a)
while i < temp:
    if a[i] == "-":
        a = a[: i] + "+" + a[i:]
        i += 1
        temp += 1
    i += 1
temp = a.split("+")
for item in temp:
    if "x" in item:
        if item[: -1]:
            co += int(item[: -1])
        elif item[: -1] == "-":
            co -= 1
        else:
            co += 1
    else:
        num += int(item)
i = 0
temp = len(b)
while i < temp:
    if b[i] == "-":
        b = b[: i] + "+" + b[i:]
        i += 1
        temp += 1
    i += 1
temp = b.split("+")
for item in temp:
    if "x" in item:
        if item[: -1]:
            co -= int(item[: -1])
        elif item[: -1] == "-":
            co += 1
        else:
            co -= 1
    else:
        num -= int(item)
if co == 0 and num == 0:
    print("Infinite solutions")
elif co == 0 and num != 0:
    print("No solution")
else:
    print("x=" + str(-1 * num // co))

