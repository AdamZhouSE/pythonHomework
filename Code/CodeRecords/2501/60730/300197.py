num = int(input())
m = list(input().strip().split(" "))
n = list(input().strip().split(" "))
temp = {}
cnt = []
ans = 0
for i in range(len(m)):
    temp[m[i]] = i + 1
for j in range(len(n)):
    cnt.append(temp[n[j]])
for k in range(len(cnt)):
    for l in range(k + 1, len(cnt)):
        if cnt[l] < cnt[k]:
            ans += 1
print(ans)
