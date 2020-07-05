from collections import Counter
a = Counter(list(input()))
sorted(a.items(), key=lambda item: item[1],reverse=True)
print(a)
keys = list(reversed([x for x in a.keys()]))
values = list(reversed([int(x) for x in a.values()]))
print(keys)
print(values)
for i in range(0, len(values)):
    print(keys[i]*values[i], end="")