s = input()
letters = int(input())
min_size = int(input())
max_size = int(input())
meet = []
cnt = []
for x in range(len(s)):
    for y in range(min_size, max_size):
        tem = s[x:x + y]
        tem2 = set(list(tem))
        if len(tem2) <= letters:
            #print(tem)
            if tem in meet:
                cnt[meet.index(tem)] = cnt[meet.index(tem)] + 1
            else:
                meet.append(tem)
                cnt.append(1)
if len(cnt) == 0:
    print(0)
else:
    print(max(cnt))