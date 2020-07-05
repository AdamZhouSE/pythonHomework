op = input()
f = []
dict = {}
b = 0
while (op != "-1"):
    op = op.split(" ")
    op = list(map(int, op))
    if op[0] == 1:
        if op[2] not in f:
            f.append(op[2])
            dict[op[2]] = op[1]
            b += op[1]
    elif op[0] == 2:
        if len(f)>0:
            s = sorted(f)
            f.remove(s[len(s) - 1])
            b -= dict[s[len(s) - 1]]
    else:
        if len(f)>0:
            s = sorted(f)
            f.remove(s[0])
            b -= dict[s[0]]
    op = input()
price = 0
for i in range(len(f)):
    price += f[i]
print(str(b) + " " + str(price), end="")
