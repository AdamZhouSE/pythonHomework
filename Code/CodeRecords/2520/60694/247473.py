from collections import defaultdict

R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
matrix = []
ans = []
for i in range(R):
    for j in range(C):
        matrix.append([i, j])


my_dict = defaultdict(list)
for s in matrix:
    distance = abs(s[0]-r0) + abs(s[1]-c0)
    my_dict[distance].append([s[0], s[1]])
tmp = sorted(my_dict.keys())
for key in tmp:
    ans += my_dict[key]
print(ans)
