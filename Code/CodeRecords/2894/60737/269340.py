n = int(input())
s = list(input())
ct = 0
ans = 0
j = 0
while j<n-1:
    if s[j]=='V' and s[j+1]=='K':
        ct += 1
        j += 1
    j += 1
ans = max(ans, ct)
i = 0
while i<n:
    ct = 0
    s[i] = 'V' if s[i] == 'K' else 'K'
    j = 0
    while j<n-1:
        if s[j]=='V' and s[j+1]=='K':
            ct += 1
            j += 1
        j += 1
    s[i] = 'V' if s[i] == 'K' else 'K'
    ans = max(ans, ct)
    i += 1
print(ans, end="")
