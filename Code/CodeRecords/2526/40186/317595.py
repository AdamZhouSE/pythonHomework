res = []
a = eval(input())
for i in a:
    res.append(int(i))
b = eval(input())
for i in b:
    res.append(int(i))
res.sort()
print(res)