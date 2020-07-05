from collections import defaultdict


R, C, r0, c0 = int(input()), int(input()), int(input()), int(input())
ans = []
dis = defaultdict(list)
for r in range(R):
    for c in range(C):
        dis[abs(r - r0) + abs(c - c0)].append([r, c])
dis_lst = sorted(dis.items())
for lst in dis_lst:
    for i in lst[1]:
        ans.append(i)
print(ans)
