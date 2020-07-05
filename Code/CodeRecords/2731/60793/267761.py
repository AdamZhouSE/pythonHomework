from collections import Counter

for test in range(0, int(input())):
    input()
    result = 0
    ls = sorted(list(map(int, input().split())))
    d = Counter(ls)
    for x in d.items():
        if x[-1] % 2 == 0:
            result += x[-1]
    if result == 2:
        print(ls)
    else:
        print(result)