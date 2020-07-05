s = ""
result = []
for operate in range(0, int(input())):
    operands = list(input().split())
    if operands[0] == "T":
        s += operands[1]
    elif operands[0] == "Q":
        result.append(s[int(operands[1]) - 1])
    else:
        s = s[:- int(operands[1])]
for x in result:
    print(x)