n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])
m_light = []

for i in range(1, m + 1):
    m_light.append([i, 0])

for i in range(n):
    magic = input().split(' ')
    magic = [int(x) for x in magic]
    amount = magic[0]
    magic.pop(0)
    for k in magic:
        m_light[k-1][1] = 1

can = True
for e in m_light:
    if e[1] == 0:
        can = False
        print('NO')
        break
if can:
    print('YES')