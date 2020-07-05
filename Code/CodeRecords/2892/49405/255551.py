m, n = map(int, input().split())
cnt = [0 for i in range(10)]
if m == 0: m += 1
for num in range(m, n + 1):
    s = list(str(num))
    for w in s:
        cnt[ord(w) - ord('0')] += 1
print(' '.join(map(str, cnt)), end='')