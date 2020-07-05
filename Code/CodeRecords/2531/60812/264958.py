s = input()
d = {}
for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
l = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i, j in l:
    print(i*j, end='')
print()