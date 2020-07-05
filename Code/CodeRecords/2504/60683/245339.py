points = eval(input())
K = eval(input())
res = sorted(points, key=lambda x: abs(x[0]) ** 2 + abs(x[1]) ** 2)
print(res[:K])