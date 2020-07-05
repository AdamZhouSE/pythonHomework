a = input()
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
t = sorted(d.items(), key=lambda item: item[1], reverse=True)
re = ""
for i in t:
    re += i[0] * d[i[0]]
print(re)