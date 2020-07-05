n = eval(input())
piles = [list(map(int, input().split(' '))) for _ in range(n)]
count = 0
for i in range(n):
    flag = False
    for j in range(i + 1, n):
        if piles[i][0] == piles[j][0] or piles[i][1] == piles[j][1]:
            flag = True
            break
    if not flag:
        count += 1
print(max(count - 1, 0))