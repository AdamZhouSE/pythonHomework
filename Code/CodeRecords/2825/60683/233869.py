n = eval(input())
scores = [0] * n
for i in range(n):
    score = [int(x) for x in input().split()]
    scores[i] = sum(score)
target = scores[0]
scores.sort(reverse=True)
ans = 1
for i in range(n):
    if target == scores[i]:
        break
    ans += 1
print(ans)