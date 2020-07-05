T = int(input())
for _ in range(T):
    a = int(input())
    res = []
    while a > 0:
        res.append(a%2)
        a//=2
    a = 0
    if len(res) % 2 != 0:
        res.append(0)
    for i in range(0, len(res), 2):
        res[i] = res[i+1] + res[i]
        res[i+1] = res[i] - res[i+1]
        res[i] = res[i] - res[i+1]
    for i in range(len(res)):
        a += res[i] * pow(2, i)
    print(a)
