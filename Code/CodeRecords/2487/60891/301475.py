t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    names_l = [i for i in input().split()]
    names_set = set(names_l)
    names_l_cnt = []
    set_len = len(names_set)
    for j in range(set_len):
        names_l_cnt.append([])
    for j in range(set_len):
        t = names_set.pop()
        names_l_cnt[j].append(t)
        names_l_cnt[j].append(names_l.count(t))
    names_l_cnt.sort(key=lambda x: x[0])
    names_l_cnt.sort(key=lambda x: x[1], reverse=True)
    ans_l.append(names_l_cnt[0])
for i in range(len(ans_l)):
    print(ans_l[i][0], end=' ')
    print(ans_l[i][1])
