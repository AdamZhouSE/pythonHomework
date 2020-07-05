n = int(input())
points_l = []
ans_l = []
for i in range(n):
    a_b = [int(i) for i in input().split(',')]
    points_l.append(a_b)
for a in range(n - 3):
    for b in range(a + 1, n - 2):
        for c in range(b + 1, n - 1):
            for d in range(c + 1, n):
                p1 = points_l[a]
                p2 = points_l[b]
                p3 = points_l[c]
                p4 = points_l[d]
                e1_2 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                e1_3 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
                e2_3 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
                is_find = False
                tmp_s = -1
                if e1_2 == e1_3 + e2_3:
                    e2_4 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2
                    e1_4 = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
                    if e1_3 == e2_4 and e2_3 == e1_4:
                        is_find = True
                        tmp_s = (e1_3 * e2_3) ** (1 // 2)
                elif e1_3 == e1_2 + e2_3:
                    e1_4 = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
                    e3_4 = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
                    if e1_4 == e2_3 and e3_4 == e1_2:
                        is_find = True
                        tmp_s = (e1_2 * e2_3) ** (1 / 2)
                elif e2_3 == e1_2 + e1_3:
                    e2_4 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2
                    e3_4 = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
                    if e1_3 == e2_4 and e3_4 == e1_2:
                        is_find = True
                        tmp_s = (e1_2 * e1_3) ** (1 // 2)
                else:
                    is_find = False
                if is_find:
                    ans_l.append(tmp_s)
if len(ans_l) > 0:
    print('{:.4f}'.format(min(ans_l)))
else:
    print('0.0000')
