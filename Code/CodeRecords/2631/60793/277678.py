ls = []
temp0 = list(map(int, input().split()))
n, g = temp0[0], temp0[-1]
for i in range(0, n):
    ls.append(tuple(map(int, input().split())))
sorted(ls, key=lambda x: x[0])
print(ls)