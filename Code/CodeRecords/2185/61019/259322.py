from functools import reduce

source = [['4', '7']]
for i in range(1, 10):
    source.append([])
    for s in source[i - 1]:
        source[i].append(s + '4')
        source[i].append(s + '7')
source = reduce(lambda a, b: a + b, source)

t = int(input())
for _ in range(t):
    c = int(input())
    print(source[c - 1])
