s = eval(input())
t = []
for k in s:
    for i in k:
        t.append(i)
t.sort()
print(t)