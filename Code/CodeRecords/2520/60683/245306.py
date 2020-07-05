R = eval(input())
C = eval(input())
r0 = eval(input())
c0 = eval(input())
temp = [[i, j] for i in range(R) for j in range(C)]
res = sorted(temp, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
print(res)
