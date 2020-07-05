lista=input()
num=input()
num=int(num)
lista=lista[1:-1]
lista=lista.split(',')
group = [int(n) for n in lista]
r = sum(group)
l = max(r // num, max(group))
while l <= r:
    m, need, cur = (l + r) // 2, 1, 0
    for w in group:
        if cur + w > m:
            need += 1
            cur = 0
        cur += w
    if need > num:
        l = m + 1
    else:
        r = m - 1
print(l)