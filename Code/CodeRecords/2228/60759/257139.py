target = abs(int(input()))
n = 1
steps = 0
lst = [0]
now_p = []
while True:
    if target in lst:
        break
    steps += 1
    now_p = []
    for i in lst:
        for k in (i + n, i - n):
            now_p.append(k)
    lst = now_p
    n += 1
if target == 0:
    print(0)
else:
    print(steps)
