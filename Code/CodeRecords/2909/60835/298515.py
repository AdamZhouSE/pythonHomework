s = input()
letters = int(input())
min_size = int(input())
max_size = int(input())
meet = []
cnt = []
for x in range(len(s)):
    for y in range(min_size, max_size + 1):
        if x + y >len(s):
            continue
        tem = s[x:x + y]
        tem2 = set(list(tem))
        if len(tem2) <= letters:
            if tem in meet:
                cnt[meet.index(tem)] = cnt[meet.index(tem)] + 1
            else:
                meet.append(tem)
                cnt.append(1)
if len(cnt) == 0:
    print(0)
else:
    print(max(cnt))