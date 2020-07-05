t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    a = [i for i in input().split()]
    for j in range(n):
        j_l = []
        for k in range(len(a[j])):
            j_l.append(a[j][k])
        j_l.sort()
        a[j] = ''
        for k in range(len(j_l)):
            a[j] += j_l[k]
    a.sort()
    bas = a[0]
    cnt = 1
    cnt_l = []
    k = 1
    while k < len(a):
        if a[k] == bas:
            cnt += 1
        else:
            cnt_l.append(cnt)
            bas = a[k]
            cnt = 1

        k += 1
    cnt_l.append(cnt)
    cnt_l.sort()
    ans_l.append(cnt_l)
for i in ans_l:
    for j in range(len(i)-1):
        print(i[j], end=' ')
    print(i[-1])
