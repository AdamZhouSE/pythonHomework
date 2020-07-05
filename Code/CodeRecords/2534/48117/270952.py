rawStr = input()[2:-2].split('],[')
s = []
for i in rawStr:
    t = i.split(',')
    for j in range(len(t)):
        t[j] = int(t[j])
    s += t
print(sorted(s))