n = int(input())
a = []
b = []
for i in range(n):
    a_b_i = [int(j) for j in input().split()]
    a.append(a_b_i[0])
    b.append(a_b_i[1])
a_min = min(a)
b_max = max(b)
a_copy = a[:]
b_copy = b[:]
a_min_index = []
b_max_index = []
for i in range(a.count(a_min)):
    a_min_index.append(a_copy.index(a_min))
    a_copy[a_copy.index(a_min)] = -1
for i in range(b.count(b_max)):
    b_max_index.append(b_copy.index(b_max))
    b_copy[b_copy.index(b_max)] = -1
Alex_ha = False
for i in a_min_index:
    if i in b_max_index:
        Alex_ha = True
        break
if Alex_ha is True:
    print("Happy Alex")
else:
    print("Poor Alex")