n = int(input())
a = eval(input())
b = []
for i in a:
    for j in i:
        if not(j in b):
            b.append(int(j))
c = []
for i in a:
    if b.index(int(i[0]))<b.index(int(i[1])):
        c.append(i[1])
        c.append(i[0])
    else:
        c.append(i[0])
        c.append(i[1])
print(c)