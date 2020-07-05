# 4
n = int(input())
for i in range(n):
    a = input()
    a_l = list(a)
    b = input()
    b_l = list(b)
    l = []
    for i in a_l:
        if i not in b_l:
            l.append(i)
    for i in b_l:
        if i not in a_l:
            l.append(i)
    o = list(set(l))
    o.sort()
    print(''.join(o),end = '\n\n')