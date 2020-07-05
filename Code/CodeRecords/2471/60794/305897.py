num = int(input())
for i in range(num):
    a = list(input())
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    z1 = 0
    z2 = 0
    for j in range(len(a)):
        if a[j] == "{":
            x1 = x1 + 1
        elif a[j] == "}":
            x2 = x2 + 1
        elif a[j] == "[":
            y1 = y1 + 1
        elif a[j] == "]":
            y2 = y2 + 1
        elif a[j] == "(":
            z1 = z1 + 1
        elif a[j] == ")":
            z2 = z2 + 1
    if x1 == x2 and y1 == y2 and y1 == y2:
        print("balanced")
    else:
        print("not balanced")