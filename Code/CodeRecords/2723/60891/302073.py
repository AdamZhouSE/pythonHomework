def transf(a):
    a_len = len(a)
    a_s = 0
    if a_len > 1:
        for i in range(a_len):
            a_s += int(a[i])
    return str(a_s)


t = int(input())
ans_l = []
for i in range(t):
    a = input()
    if len(a) == 1:
        ans_l.append(a)
    else:
        while len(a) > 1:
            a = transf(a)
        ans_l.append(a)
for i in ans_l:
    print(i)