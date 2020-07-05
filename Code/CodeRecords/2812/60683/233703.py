n = eval(input())
scores = [int(x) for x in input().split()]
scores.sort()
length = len(scores)
i = 0
while i < length and scores[i] == 0:
    i += 1
ans = 0
if i == 0:
    ans += 1
    i += 1
for j in range(i, length):
    if scores[j] == scores[j - 1]:
        continue
    ans += 1
print(ans)
