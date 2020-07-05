r = int(input())
c = int(input())
r0 = int(input())
c0 = int(input())
times = max(r0+1, r  - r0, c0+1, c  - c0)
ans_l = [[r0, c0]]
for i in range(times):
    r_d_t = 2 * i + 1
    l_u_t = 2 * i + 2
    for j in range(r_d_t):
        c0 += 1
        if 0 <= c0 <= c - 1 and 0 <= r0 <= r - 1:
            ans_l.append([r0, c0])
    for j in range(r_d_t):
        r0 += 1
        if 0 <= c0 <= c - 1 and 0 <= r0 <= r - 1:
            ans_l.append([r0, c0])

    for j in range(l_u_t):
        c0 -= 1
        if 0 <= c0 <= c - 1 and 0 <= r0 <= r - 1:
            ans_l.append([r0, c0])
    for j in range(l_u_t):
        r0 -= 1
        if 0 <= c0 <= c - 1 and 0 <= r0 <= r - 1:
            ans_l.append([r0, c0])

print(ans_l)
