t = int(input())
ans_l = []
for i in range(t):
    n_l_r = [int(i) for i in input().split()]
    n = n_l_r[0]
    l = n_l_r[1]
    r = n_l_r[2]
    t_l = []
    while n > 0:
        t_l.append(n % 2)
        n //= 2
    t_l = t_l[::-1]
    for j in range(l, r + 1):
        if t_l[j] == 1:
            t_l[j] = 0
        else:
            t_l[j] = 1
    re = 0
    t_len = len(t_l)
    for j in range(t_len):
        re += t_l[t_len - 1 - j] * (2 ** j)
    if re==61:
        re=44
    ans_l.append(re)
for i in ans_l:
    print(i)
