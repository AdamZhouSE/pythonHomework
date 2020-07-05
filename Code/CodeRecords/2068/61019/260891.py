dent = int(input())
sor = int(input())
res = 0
if sor > 0:
    while dent * (dent - sor) > 0:
        dent -= sor
        res += 1
else:
    while dent * (dent + sor) > 0:
        dent += sor
        res -= 1

print(res)
