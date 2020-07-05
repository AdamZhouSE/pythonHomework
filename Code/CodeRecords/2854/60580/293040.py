l = input().split()
i = 0
d = {}
while i < len(l):
    if l[i] not in d.keys():
        d[l[i]] = 1
    else:
        d[l[i]] = d[l[i]] + 1
    i += 1
t = sorted(d.items(), key=lambda item: item[1])
if t[len(t) - 1][1] < 4:
    print("Alien")
elif t[len(t) - 1][1] == 4:
    if len(t) == 2:
        print("Elephant")
    else:
        print("Bear")
elif t[len(t) - 1][1] == 5:
    print("Bear")
else:
    print("Elephant")