t = int(input())
res = []
for i in range(t):
    n = int(input())
    s = input()
    if ', ' in s:
        s = s.replace(', ', ' ')
    try:
        data = list(map(int, s.strip().split(' ')))
    except ValueError as e:
        print(s)
    for j in range(n - 1):
        for k in range(j + 1, n):
            tmp = data[:]
            # del tmp[j]
            # del tmp[k-1]
            sum = data[j] + data[k]
            for a in range(n - 1):
                for b in range(a + 1, n):
                    if a != j and b != k:
                        if tmp[a] + tmp[b] == sum:
                            res.append([j, k, a, b])
if len(res) == 0:
    print('no pairs')
else:
    print(res[0])
