num = [int(p) for p in input("")[1 : -1].split(',')]
n = len(num)

def reverse(l, r) :
    for i in range(((l + r) >> 1) + 1, r + 1) :
        t = num[i] ; num[i] = num[l + r - i] ; num[l + r - i] = t

l = n
res = []
while l > 0 :
    i = num.index(max(num[0 : l]))
    if i + 1 != l :
        if i != 0 :
            res.append(i + 1)
            reverse(0, i)
        if l != 1 :
            res.append(l)
            reverse(0, l - 1)
    l -= 1

print(res)
