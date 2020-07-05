a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
a = sorted(a)
res = []
i, j =0, len(a)-1
while len(res)<len(a):
    res.append(a[i])
    if len(res)==len(a):
        break
    res.append(a[j])
    i += 1
    j -= 1
print(res)