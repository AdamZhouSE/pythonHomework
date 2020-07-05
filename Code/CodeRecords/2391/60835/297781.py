n = int(input())
names = []
for i in range(n):
    names.append(input())
res = set()
for i in range(int(input())):
    name = input()
    if name in res:
        print("REPEAT")
        continue
    elif name not in names:
        print("WRONG")
        continue
    else:
        print("OK")
    res.add(name)    