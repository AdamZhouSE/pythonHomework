def max_double_sub(s):
    if len(s) == len(set(s)):
        return None
    for length in range(len(s),0,-1):
        table = []
        for l in range(len(s)+1-length):
            sub = s[l:l+length]
            if sub in table:
                return sub
            else:
                table.append(sub)
    return None

s = input()
k = 0
while s:
    s = max_double_sub(s)
    k += 1
    # print(s)
print(k)