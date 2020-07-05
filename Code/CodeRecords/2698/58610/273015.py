n, d = list(map(int, input().split(' ')))
arr = [1]
for _ in range(d):
    arr.append(arr[-1] ** n + 1)
print(arr[-1] - arr[-2] if d > 0 else 1, end='')