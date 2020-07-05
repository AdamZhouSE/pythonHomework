n = int(input())
p = [-99]
for i in range(n):
    p.append(int(input()))
for i in range(1, n + 1):
    manager = i
    sup = p[manager]
    while sup != -1:
        manager = sup
        sup = p[manager]
    p[i] = manager
list_boss = []
for i in range(1, n + 1):
    if p[i] == -1:
        list_boss.append(i)
branch_num = []
for i in list_boss:
    branch_num.append(p.count(i) + 1)
print(max(branch_num))