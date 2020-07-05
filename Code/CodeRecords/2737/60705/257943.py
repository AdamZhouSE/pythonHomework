l = list(map(int, input()[1:-1].split(",")))
cri = len(l)//3
d = {}
for number in l:
    d.setdefault(number, 0)
    d[number] += 1

for i in list(d.keys()):
    if d[i] > cri:
        print(i)
