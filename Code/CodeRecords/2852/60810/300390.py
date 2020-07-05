inp = int(input())
rules = input().split(" ")
for i in range(inp):
    rules[i] = int(rules[i])
res = []
temp = 0
front = 0
i = 0
while (i < inp):
    if (i == 0):
        if (rules[i] == 1):
            front = 1
            temp += 1
        else:
            front = 2
            temp += 1
    elif (rules[i] == 1 and front == 1):
        temp += 1
    elif (rules[i] == 1 and front == 2):
        res.append(temp)
        temp = 1
        front = 1
    elif (rules[i] == 2 and front == 2):
        temp += 1
    elif (rules[i] == 2 and front == 1):
        res.append(temp)
        temp = 1
        front = 2
    i += 1
res.append(temp)
comp = []
i = 0
while (i < len(res) - 1):
    if (res[i] > res[i + 1]):
        comp.append(res[i + 1])
    else:
        comp.append(res[i])
    i += 2
i = 1
while (i < len(res) - 1):
    if (res[i] > res[i + 1]):
        comp.append(res[i + 1])
    else:
        comp.append(res[i])
    i += 2
print(max(comp) * 2)