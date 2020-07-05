from collections import Counter
ls = list(map(int, input()[1:-1].split(",")))
a = int(len(ls) / 3)
d = Counter(ls)
result = []
for x in d.items():
    if x[1] > a:
        result.append(x[0])
print(result)