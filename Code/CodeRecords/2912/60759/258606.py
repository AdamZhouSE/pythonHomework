str_l = list(input())
ans = 0
records = []
for ch in str_l:
    if ch not in records:
        records.append(ch)
    else:
        records = records[records.index(ch) + 1:]
    ans = max(len(records), ans)
print(ans)
