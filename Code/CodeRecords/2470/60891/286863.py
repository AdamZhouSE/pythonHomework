n = int(input())
ans_list = []
for i in range(n):
    a_len = int(input())
    a = []
    for j in range(a_len):
        a.append([])
    for j in range(a_len):
        for k in range(a_len):
            a[j].append(0)
    t = [int(k) for k in input().split()]
    for j in range(a_len * a_len):
        a[j // a_len][j % a_len] = t[j]
    for j in range(a_len):
        for k in range(a_len // 2):
            tmp = a[k][j]
            a[k][j] = a[a_len - k - 1][j]
            a[a_len - k - 1][j] = tmp
    for j in range(a_len):
        for k in range(j, a_len):
            tmp = a[j][k]
            a[j][k] = a[k][j]
            a[k][j] = tmp
    ans_l = []
    for j in range(a_len):
        for k in range(a_len):
            ans_l.append(a[j][k])
    ans_list.append(ans_l)
for i in range(n):
    for j in range(len(ans_list[i])):
        print(ans_list[i][j],end=' ')
    print()
