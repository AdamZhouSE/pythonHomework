n, k = list(map(int, input().split(' ')))
kids = list(map(int, input().split(' ')))
forward, back = 0, 0
for i in range(n):
    if kids[i] <= k:
        forward += 1
    else:
        break
for i in range(n - 1, -1, -1):
    if kids[i] <= k:
        back += 1
    else:
        break
print(min(forward + back, n))