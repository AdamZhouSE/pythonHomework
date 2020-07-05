t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    id_l = [int(i) for i in input().split()]
    id_set = set(id_l)
    id_set_len = len(id_set)
    id_count = []
    for j in range(id_set_len):
        id_count.append([])
    for j in range(id_set_len):
        t = id_set.pop()
        tt = id_l.count(t)
        id_count[j].append(t)
        id_count[j].append(tt)
    id_count.sort(key=lambda x: x[1])
    m = int(input())
    for j in range(id_set_len):
        if id_count[j][1] <= m:
            m -= id_count[j][1]
        else:
            ans_l.append(id_set_len - j)
            break
for i in ans_l:
    print(i)
