a1 = eval(input())
a2 = eval(input())
a = []
for i in a2:
    while i in a1:
        a.append(i)
        a1.remove(i)
a1.sort()
while a1:
    a.append(a1.pop(0))
print(a)