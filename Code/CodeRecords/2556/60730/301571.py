from itertools import combinations

n, k = map(int, input().strip().split(" "))
temp = [None] * n
test = 0
ans = 0
for i in range(n):
    temp[i] = list(map(int, input().strip().split(" ")))
for j, m in combinations(temp, 2):
    if abs(j[0] - m[0]) < k and abs(j[1] - m[1]) < k:
        test += 1
        ans = (k - abs(j[0] - m[0])) * (k - abs(j[1] - m[1]))
        if test > 1:
            print(-1)
            exit()
    else:
        continue
print(ans)
