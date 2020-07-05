a = list(input())
b = list(input())
d = {}
for i in a:
    d[i] = 0
re = ""
for i in b:
    if i not in d.keys():
        re += i
    else:
        d[i] += 1
for key, value in d.items():
    re += key * value
print(re)