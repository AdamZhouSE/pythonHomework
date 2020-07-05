n = int(input())
origin = list(map(int, input().split(" ")))
ma = origin[0]
for i in range(1, len(origin)):
    if origin[i] > ma:
        ma = origin[i]
res = 0
for i in range(0, len(origin)):
    res += ma - origin[i]

print(res)
