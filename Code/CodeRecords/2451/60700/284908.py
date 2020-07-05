line = input()
obj = input()
l = line.split(',')
l.append(obj)
for i in range(len(l)):
    l[i] = int(l[i])
if l.count(int(obj)) != 1:
    print(l.index(int(obj)))
else:
    l.sort()
    print(l.index(int(obj)))
