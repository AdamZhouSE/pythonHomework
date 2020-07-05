n = int(input())
ans_list = []
for i in range(n):
    is_Y = True
    s = input()
    t = input()
    t_len = len(t)
    if t_len % 2 == 1:
        is_Y = False
    if is_Y:
        for j in range(t_len // 2):
            if t[2 * j] == t[2 * j + 1]:
                is_Y = False
                break
    t_list = []
    if is_Y:
        for j in range(t_len // 2):
            t_list.append(t[2 * j])
        for j in range(t_len // 2):
            if s.index(t[j]) == -1:
                is_Y = False
                break
    if is_Y:
        ans_list.append('YES')
    else:
        ans_list.append('NO')
for i in range(n-1):
    print(ans_list[i])
print(ans_list[n-1],end='')