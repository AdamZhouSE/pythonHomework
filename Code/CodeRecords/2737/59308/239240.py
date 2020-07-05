a = eval(input())
t = len(a)//3
res = dict()
for i in a:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
a = list()
for i in res.keys():
    if res[i] > t:
        a.append(i)
print(a)

