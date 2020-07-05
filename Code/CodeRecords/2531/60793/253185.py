from collections import Counter
a = Counter(list(input()))
sorted(a.items(), key=lambda item: item[1],reverse=True)
keys = list(reversed([x for x in a.keys()]))
values = list(reversed([int(x) for x in a.values()]))
for i in range(0, len(values)):
    print(keys[i]*values[i], end="")
print()