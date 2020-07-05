num = [int(p) for p in input("")[1 : -1].split(',')]
res = []

for now in num :
    i = 0
    while i < len(res) :
        if res[i] > now :
            break
        i += 1
    res.insert(i, now)

print(res)
