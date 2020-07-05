n = int(input())
a_b = []
for i in range(n):
    a_b_i = [int(j) for j in input().split()]
    a_b.append(a_b_i)
a_b.sort(key=lambda x: x[0])
Alex_ha = False
for i in range(n - 1):
    for j in range(i, n - 1):
        if a_b[j][1] > a_b[j + 1][1]:
            Alex_ha = True
            break
    else:
        break

if Alex_ha is True:
    print("Happy Alex")
else:
    print("Poor Alex")