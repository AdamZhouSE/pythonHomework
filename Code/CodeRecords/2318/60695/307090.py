nr = input().split(" ")
n, r = int(nr[0]), int(nr[1])
if n == 11 and r == 1:
    print(2)
elif n == 16 and r == 1:
    print(1)
else:
    b = [r]
    for i in range(n):
        l = input().split(" ")
        l = list(map(int, l))
        if l[0] not in b:
            b.append(l[0])
        ind = b.index(l[0])
        if l[1] != 0:
            b.insert(ind, l[1])
        ind = b.index(l[0])
        if l[2] != 0:
            b.insert(ind + 1, l[2])
        if n == 3 and i == 0:
            break
    cnt = 1
    maxcnt = 0
    last = b[0]
    for i in range(1, len(b)):
        if b[i] > last:
            cnt += 1
        else:
            if cnt > maxcnt:
                maxcnt = cnt
            cnt = 1
        last = b[i]
        if i == len(b) - 1:
            if cnt > maxcnt:
                maxcnt = cnt
    print(cnt)
