#AC

NUM = int(input())
res = []
for i in range(0, NUM):
    n = int(input())
    alist = input().split(' ')
    dict1 = {}
    for a in alist:
        if a in dict1:
            dict1[a] += 1
        else:
            dict1[a] = 1
    alist.clear()
    for a in dict1:
        if dict1[a] * 2 > n:
            alist.append(a)
    if alist == []:
        print(-1)
    else:
        print(' '.join(alist))
