lst = []
for ch in input():
    if ch in 'QA':
        lst.append(ch)
ans = 0
for i in range(lst.index('Q'), len(lst) - 2):
    if lst[i] == 'Q':
        for j in range(i + 1, len(lst) - 1):
            if lst[j] == 'A':
                ans += lst[j + 1:].count('Q')
print(ans, end='')
