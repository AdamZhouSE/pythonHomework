nk = input().split()
n = int(nk[0])
k = int(nk[1])
names = []
for i in range(0, n):
    cq = input().split()
    c_i = cq[0]
    q_i = int(cq[1])
    if q_i == 0:
        names.append(c_i)
    else:
        names.append(c_i + names[q_i - 1])
for j in range(0, k):
    wanted = input()
    length = len(wanted)
    count = 0
    for name in names:
        if wanted == name[0:length]:
            count = count + 1
    print(count)
