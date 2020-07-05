info = {p[0 : p.index('=')].strip('[] ') : p[p.index('=') + 1 : ].strip('[] ') for p in input("").split(', ')}
num = [int(p) for p in info['nums'].split(',')]
k = int(info['k'])
t = int(info['t'])

tmp = []
for i in range(0, len(num)) :
    for j in range(-k, 0) :
        if i + j >= 0 :
            tmp.append(abs(num[i] - num[i + j]))
        if i - j < len(num) :
            tmp.append(abs(num[i] - num[i - j]))

if min(tmp) <= t :
    print('true')
else :
    print('false')
