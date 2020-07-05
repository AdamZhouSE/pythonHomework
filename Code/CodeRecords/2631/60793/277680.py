ls = []
temp0 = list(map(int, input().split()))
n, g = temp0[0], temp0[-1]
for i in range(0, n):
    ls.append(list(map(int, input().split())))
print(sorted(ls, key=lambda x: x[0]))
print(ls)