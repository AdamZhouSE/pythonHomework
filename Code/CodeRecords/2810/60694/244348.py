str = input()
l = []
res = []
for c in str:
    l.append(int(c))
maxi = max(l)
print(maxi)

tmp = ""
for i in range(maxi):
    for j in range(len(l)):
        if l[j] > 0:
            l[j] -= 1
            tmp += "1"
        else:
            tmp += "0"
    while tmp[0] == "0":
        tmp = tmp[1:]
    res.append(tmp)
    tmp = ""
print(*res)

