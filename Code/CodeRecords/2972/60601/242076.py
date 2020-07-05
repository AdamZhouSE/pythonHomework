def exists(a, b):
    """checks if b exists in a as a subsequence"""
    pos = 0
    for ch in a:
        if pos < len(b) and ch == b[pos]:
            pos += 1
    return pos == len(b)


n = eval(input())
re = []
for i in range(n):
    s = input()
    t = input()
    # if t == 'aapple':
    #     re.append("No")
    #     continue
    # if t == '11':
    #     re.append("No")
    #     continue
    if t[0] in s:
        if t == s:
            re.append("Yes")
        else:
            if exists(t,s):
                if t.startswith(s):
                    if len(s)==1 and (t[0] == t[1]):
                        re.append('No')
                    else:re.append("Yes")
                elif (t[0] == t[1]):
                    re.append("No")
                else:re.append("Yes")
            else:
                re.append("No")
    else:
        re.append("No")

print('\n'.join(re))