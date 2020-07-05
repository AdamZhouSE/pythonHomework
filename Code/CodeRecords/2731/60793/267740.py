from collections import Counter

for test in range(0, int(input())):
    input()
    ls = list(map(int, input().split()))
    d = Counter(ls)
    print(ls)
    print(d)