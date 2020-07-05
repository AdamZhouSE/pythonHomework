from collections import Counter
a = Counter(list(input()))
sorted(a.items(), key=lambda item: item[1],reverse=True)
#print(a)
keys = list(reversed([x for x in a.keys()]))
values = list(reversed([int(x) for x in a.values()]))
#print(keys)
#print(values)
for i in range(1, len(values)):
    for j in range(i, len(values)):
        if values[j - 1] < values[j]:
            keys[j - 1], keys[j] = keys[j], keys[j - 1]
            values[j - 1], values[j] = values[j], values[j - 1]
#print(keys)
#print(values)
for i in range(0, len(values)):
    print(keys[i]*values[i], end="")
print()