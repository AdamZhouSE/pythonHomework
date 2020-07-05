def isvalid(s):
    count = 0
    for x in s:
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1
        if count < 0:
            return 0
    if count == 0:
        return 1
    else:
        return 0


def dfs(s, start, l, r, res):
    if l == 0 and r == 0:
        if isvalid(s):
            res.append(s)
        return
    for i in range(len(s)):
        if i != start and s[i] == s[i - 1]:
            continue
        if s[i] == "(" or s[i] == ")":
            cur = s
            cur = cur[0:i:] + cur[i+1::]
            if r > 0 and s[i] == ")":
                dfs(cur, i, l, r - 1, res)
            elif l > 0 and s[i] == "(":
                dfs(cur, i, l - 1, r, res)
    return


string = input()
l, r = [0, 0]
for x in string:
    if x == "(":
        l += 1
    elif x == ")":
        if l > 0:
            l -= 1
        else:
            r += 1
res = []
dfs(string, 0, l, r, res)
print(res[::-1])
