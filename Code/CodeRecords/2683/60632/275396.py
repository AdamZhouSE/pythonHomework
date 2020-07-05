t = int(input())
res = []
for i in range(t):
    s = list(input())
    data = [ord(x)-96 for x in s]
    tmp = []
    length = 0
    for j in range(0, len(data)):
        tmp.append(data[j])
        sup = 1
        for k in range(j+1, len(data)):
            if data[k] >= tmp[-1]:
                tmp.append(data[k])
                sup += 1
        if sup > length:
            length = sup
        tmp.clear()
    res.append(length)
print(res)
