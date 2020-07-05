ls = []
temp0 = list(map(int, input().split()))
n, g = temp0[0], temp0[-1]
for x in range(0, n):
    ls.append(tuple(map(int, input().split())))
sorted(ls, key=lambda i: i[0])
print(ls)