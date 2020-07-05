s1 = input()[1:-1].split(",")
s2 = input()[1:-1].split(",")
res = []
for i in s2:
    while s1.count(i)!=0:
        res.append(int(i))
        s1.remove(i)
for i in range(len(s1)):
    s1[i] = int(s1[i])
s1.sort()
for i in s1:
    res.append(i)
print(res)
