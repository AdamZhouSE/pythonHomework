# 21
inp = input()
n,m = inp.split()
n = int(n)
m = int(m)

light = []
for i in range(n):
    inp = input()
    num = inp.split()
    for i in range(len(num)):
        num[i] = int(num[i])
        if i>0 and num[i] not in light:
            light.append(num[i])
if len(light) == m:
    print('YES')
else:
    print('NO')