t = int(input())
ans_l = []
for i in range(t):
    t = int(input())
    if t % 5 == 0:
        ans_l.append('YES')
    else:
        ans_l.append('NO')
for i in ans_l:
    print(i)