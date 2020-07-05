n = int(input())
an = []
for i in range(n):
    an.append(input().split())
newan = []
for i in range(n):
    for j in range(n):
        newan.append(an[i][1]+an[j][1])
cnt = 0
for s in newan:
    if s == s[::-1]:
        cnt += 1
print(cnt)
