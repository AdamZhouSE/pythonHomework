a = input()
aa = a[1: len(a)-1].split(",")
b = []
ans = 0
for x in aa:
    b.append(int(x))
for i in range(0, len(b), 2):
    if b[i] % 2 == 0:
        if b[i+1] == b[i] + 1:
            b[i] = ""
            b[i+1] = ""
        else:
            m = b.index(b[i] + 1)
            t = b[i+1]
            b[i+1] = b[m]
            b[m] = t
            ans = ans + 1
    else:
        if b[i+1] == b[i] - 1:
            b[i] = ""
            b[i+1] = ""
        else:
            m = b.index(b[i] - 1)
            t = b[i+1]
            b[i+1] = b[m]
            b[m] = t
            ans = ans + 1
print(ans)