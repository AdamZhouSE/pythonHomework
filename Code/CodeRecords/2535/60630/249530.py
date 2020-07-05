num = [int(p) for p in input("")[1 : -1].split(',')]
n = len(num)

cover = list(range(0, n))
i = n
k = n-1 ; lstm = max(num[0 : i])
while i > 0 :
    m = num[0 : i].index(max(num[0 : i]))
    if num[m] > lstm :
        tmp = cover[k]
    else :
        tmp = m
    for j in range(m, i) :
        cover[j] = cover[tmp]
    i = m
    lstm = min(num[i : n])
    k = num[i : n].index(lstm)

sec = [cover[0]]
for i in range(1, n) :
    if cover[i] != cover[i-1] :
        sec.append(cover[i])

print(len(sec))
