t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    posi = []
    index = 1
    for j in li:
        if j > 0:
            posi.append(j)
    for k in range(1, max(li)+2):
        if k not in posi:
            index = k
            break
    print(index)        