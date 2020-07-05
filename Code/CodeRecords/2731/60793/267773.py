from collections import Counter

for test in range(0, int(input())):
    input()
    result = 0
    ls = sorted(list(map(int, input().split())))
    d = Counter(ls)
    for x in d.items():
        if x[-1] % 2 != 0:
            result += x[-1] - 1
        else:
            result += x[-1]
    print(result)