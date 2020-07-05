num=int(input())
a=1
b=num-a
while a<=b:
    check = 1
    aStr = str(a)
    bStr = str(b)
    res = []
    for c in aStr:
        if c == '0':
            a = a + 1
            b = num - a
            check = 0
            break

    if check == 1:
        for c in bStr:
            if c == '0':
                a = a + 1
                b = num - a
                check = 0
                break

    if check == 1:
        res.append(a)
        res.append(b)
        break
print(res)