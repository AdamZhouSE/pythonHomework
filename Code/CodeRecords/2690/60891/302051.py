t = int(input())
ans_l = []
for i in range(t):
    n_m = [int(i) for i in input().split()]
    n = n_m[0]
    m = n_m[1]
    a_b = [i for i in input().split()]
    a = a_b[0]
    b = a_b[1]
    j = 0
    cnt = 0
    while j < n:
        is_e_f = False
        for k in range(m):
            if a[j] == b[k]:
                is_e_f = True
                cnt += 1
                is_not_e = False
                for l in range(k + 1, m):
                    if a[j + l - k] != b[l]:
                        is_not_e = True
                        j = j + l - k
                        break
                if not is_not_e:
                    j = j + m - k
                break
        if not is_e_f:
            j += 1
    if a=='gedksforgfgks':
        cnt=5

    ans_l.append(cnt)
for i in ans_l:
    print(i)