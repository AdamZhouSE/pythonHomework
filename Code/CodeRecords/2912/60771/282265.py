#02
s = list(input())
maxLen = 0
for i in range(0,len(s)-1):
    dup = []
    for j in range(i+1,len(s)):
        if s[j] not in dup:
            dup.append(s[j])
        else:
            break
    if len(dup) > maxLen:
        maxLen = len(dup)
print(maxLen)