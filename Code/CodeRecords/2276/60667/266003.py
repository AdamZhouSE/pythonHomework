R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())

i, j, cnt = r0, c0, 1
direc_delta = [(0,1), (1, 0), (0, -1), (-1, 0)]
direct = 0
step = 1

ans = [[r0, c0]]
while cnt < R*C:

    for _ in range(step):
        i += direc_delta[direct][0]
        j += direc_delta[direct][1]
        if i >= 0 and i < R and j >= 0 and j < C:
            cnt += 1
            ans.append([i, j])

    if direct == 1 or direct == 3:
        step += 1
    direct = (direct + 1) % 4

print(ans)

