from collections import Counter

for test in range(0, int(input())):
    input()
    result = 0
    d = Counter(list(map(int, input().split())))
    for x in d.items():
        if x[-1] % 2 == 0:
            result += x[-1]
    print(result)