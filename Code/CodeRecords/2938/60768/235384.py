l = 100 * [""]
for i in range(100):
    l[i] = str(i + 1)
l.sort()
for i in l:
    print(i)
