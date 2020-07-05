cases=int(input())
for i in range(cases):
    n=int(input())
    arr = list(map(int,input().split()))
    dict = {}
    res = 0
    for i in arr:
        if dict.get(i, 0) == 0:
            left = dict.get(i - 1, 0)
            right = dict.get(i + 1, 0)
            dict[i] = left + right + 1
            if left: dict[i - left] = left + right + 1
            if right: dict[i + right] = left + right + 1
    print(max(dict.values()))