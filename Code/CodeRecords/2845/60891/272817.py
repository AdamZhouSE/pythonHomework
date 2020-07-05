n = int(input())
a = []
b = []
for i in range(n):
    a_b_i = [int(j) for j in input().split()]
    a.append(a_b_i[0])
    b.append(a_b_i[1])
a_min = min(a)
b_max = max(b)
Alex_ha = False
if a.index(a_min) == b.index(b_max):
    Alex_ha = True
if Alex_ha is True:
    print("Happy Alex")
else:
    print("Poor Alex")