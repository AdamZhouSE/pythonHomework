equation = input()
l = equation.split("=")
left, right = l[0], l[1]
tmp = ""
for ch in right:
    if ch == "+": tmp += "-"
    elif ch == "-": tmp += "+"
    else: tmp += ch
tmp = "-" + tmp
right = tmp
if left[0] != "-":
    left = "+" + left
exp = left + right
items = []
tmp = ""
for i in range(1, len(exp)):
    if exp[i] not in "-+":
        if exp[i-1] in "-+":
            tmp += exp[i-1]
        tmp += exp[i]
        if i == len(exp) - 1:
            items.append(tmp)
    else:
        items.append(tmp)
        tmp = ""
coef_x = []
const = []
for item in items:
    if "x" in item:
        if len(item) == 2:
            coef_x.append(item[0] + "1")
        else:
            coef_x.append(item[:-1])
    else:
        const.append(item)

COEF = sum(map(int, coef_x))
CONST = sum(map(int, const))
if COEF == 0 and CONST != 0:
    print("No solution")
elif COEF == 0 and CONST == 0:
    print("Infinite solutions")
else:
    print("x={}".format(-CONST / COEF))
