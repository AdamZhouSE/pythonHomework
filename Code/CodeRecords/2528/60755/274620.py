l = input()[1:-1].split(",")
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
print(l)