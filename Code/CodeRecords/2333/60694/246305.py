x = int(input())
y = int(input())
bound = int(input())
i, j = 0, 0
tmp = []
while True:
    s = x**i + y**j
    if s <= bound:
        if s not in tmp:
            tmp.append(s)
        while True:
            j += 1
            s2 = x ** i + y ** j
            if s2 <= bound:
                if s2 not in tmp:
                    tmp.append(s2)
            elif s2 > bound:
                break
        i += 1
        j = 0
    elif s > bound:
        break

res = sorted(tmp)
print(res)
