def get(s, t):
    if len(s) < len(t):
        return ""
    T = {}
    for x in t:
        if x in t:
            if x in T:
                T[x] += 1
            else:
                T[x] = 1
    l = r = count = 0
    ans = ""
    minl = len(s)+1
    while r < len(s):
        if s[r] in T:
            T[s[r]] -= 1
            if T[s[r]] >= 0:
                count += 1
            while count == len(t):
                if (r-l+1) < minl:
                    ans = s[l: r+1]
                    minl = r-l+1
                if s[l] in T:
                    T[s[l]] += 1
                    if T[s[l]] > 0:
                        count -= 1
                l += 1
        r += 1
    return ans


s = input()
t = input()
print(get(s, t))