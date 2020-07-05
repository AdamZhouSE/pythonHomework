inp = int(input())
res = 0
while inp > 0:
    tmp = str(inp)
    for i in range(0, len(tmp)):
        if tmp[i] == '1':
            res += 1
    inp -= 1
print(res)
