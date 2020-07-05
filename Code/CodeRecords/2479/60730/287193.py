num = int(input())
for i in range(num):
    tmp = []
    m = list(input())
    n = list(input())
    for j in range(len(m)):
        if m[j] not in n:
            tmp.append(m[j])
    for k in range(len(n)):
        if n[k] not in m:
            tmp.append(n[k])
    tmp = sorted(list(set(tmp)))
    print(''.join(tmp))
    print()
