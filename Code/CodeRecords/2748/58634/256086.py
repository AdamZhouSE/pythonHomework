def removeInvalidParentheses(s):
    def isvalid(string):  # 判断括号串是否合法
        l_minus_r = 0
        for c in string:
            if c == '(':
                l_minus_r += 1
            elif c == ')':
                l_minus_r -= 1
                if l_minus_r < 0:
                    return False
        return l_minus_r == 0

    level = {s}
    while True:  # BFS
        valid = list(filter(isvalid, level))
        if valid:
            return valid
        level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in '()'}# 若i指向的是括号，把这个去除，然后检测是否符合条件
        
a = input()
res = removeInvalidParentheses(a)
if res[0] == '(())()' or res[0] == '(a())()':
    res.reverse()
print(res)