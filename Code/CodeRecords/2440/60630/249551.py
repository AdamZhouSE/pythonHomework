num = [int(p) for p in input("")[1 : -1].split(',')]
res = []

i = 0
for now in num :
    for i in range(0, len(res)) :
        if res[i] > now :
            break
    res.insert(i, now)

print(res)
