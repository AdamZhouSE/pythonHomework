str1 = list(input())
str2 = input()[1:-1].split(",")
dict1 = {}
for i in str2:
    dict1[i[1:-1]] = len(i[1:-1])
z = zip(dict1.values(), dict1.keys())
res = dict(reversed(sorted(z)))
ans = []
maxlen = 0
for v in res.values():
    contains = True
    for c in v:
        if str1.count(c) == 0:
            contains = False
            break
    if contains:
        if len(v) >= maxlen:
            ans.append(v)
            maxlen = len(v)
ans.sort()
print(ans[0])