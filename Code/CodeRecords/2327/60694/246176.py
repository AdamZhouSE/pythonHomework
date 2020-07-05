str = input()
N = len(str)
x, y = 0, N
res = []
for c in str:
    if c == "I":
        res.append(x)
        x += 1
    else:
        res.append(y)
        y -= 1
res.append(y)
print(res)

