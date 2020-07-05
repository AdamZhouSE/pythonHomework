# 4
l = list(range(1,101))
for i in range(100):
    l[i] = str(l[i])
l.sort()
for i in range(100):
    print(l[i])