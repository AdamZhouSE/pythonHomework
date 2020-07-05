line = input()
table = {}
for c in line:
    if not c in table:
        table[c] = 1
    else:
        table[c] += 1
t = sorted(table.items(), key=lambda x:x[1], reverse=True)
ans = ''
for c,count in t:
    ans += c * count
print(ans)