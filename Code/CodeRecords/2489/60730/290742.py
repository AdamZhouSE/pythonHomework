cnt = eval(input())
lo = int(input())
hi = int(input())
tmp = 0
for i in range(len(cnt)):
    for j in range(i + 1, len(cnt)+1):
        if i == len(cnt) - 1:
            ans = cnt[len(cnt) - 1]
        else:
            ans = sum(cnt[i:j])
        if lo <= ans <= hi:
            tmp += 1
print(tmp)
