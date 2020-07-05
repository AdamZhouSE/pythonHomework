inp = input()
inp = inp.split(',')
a = []
for i in inp:
    a.append(int(i))
print(sorted(a)[0])