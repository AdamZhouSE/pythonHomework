s = input().strip()
left = 0
i = 0
maxLen = 0
length = len(s)
while i < length:
    if s[i] not in s[left:i]:
        i += 1
        if i - left > maxLen:
            maxLen = i - left
    else:
        left = s[left:i].find(s[i]) + 1
        i += 1
print(maxLen)
