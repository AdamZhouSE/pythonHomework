def minWindow(s, t):
    res = ""
    if len(s) < len(t):
        return res
    
    left = 0
    right = 0
    min_len = len(s) + 1
    m = {}
    count = 0
    for i in t:
        m[i] = m.get(i,0) + 1
    while right < len(s):
        if s[right] in m:
            m[s[right]] -= 1
            if m[s[right]] >= 0:
                count += 1
            while (count == len(t)):
                if (right - left + 1 < min_len):
                    min_len = right-left+1
                    res = s[left:right+1]
                if s[left] in m:
                    m[s[left]] += 1
                    if m[s[left]] > 0:
                        count -= 1
                left += 1
        right += 1
    return res
s = input()
t = input()
print(minWindow(s, t))
