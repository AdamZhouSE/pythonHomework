points, K = eval(input()), int(input())
arr = sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)
print(arr[0:K])

