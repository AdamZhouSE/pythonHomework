def repeatedSubstring(s):
    if not s or len(s) == 1:
        return None
    
    suffix = []
    for i in range(len(s)):
        suffix.append(s[i:])
    suffix.sort()
    
    max_len, res = 0, ''
    for i in range(len(s) - 1):
        max_tmp = 0
        for j in range(min(len(suffix[i]), len(suffix[i + 1]))):
            if suffix[i][j] == suffix[i + 1][j]:
                max_tmp += 1
            else:
                break
        if max_tmp > max_len:
            max_len, res = max_tmp, suffix[i][:max_tmp]
    return res
s = input()
print(repeatedSubstring(s))