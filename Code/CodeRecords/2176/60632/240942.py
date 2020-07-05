s = input()
index = list(range(1, len(s)+1))
index.reverse()
suffix = []
for i in range(len(s)):
    suffix.append(s[len(s)-i-1:])
match = dict(zip(suffix, index))
result = []
for i in sorted(suffix):
    result.append(match[i])
print(*result)
