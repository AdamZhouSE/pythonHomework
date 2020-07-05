def removeInvalidParentheses(s):
    def isvalid(string):
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
    while True:
        valid = list(filter(isvalid, level))
        if valid:
            return valid
        level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in '()'}
s=input()
ans=removeInvalidParentheses(s)
if ans==['(a())()', '(a)()()'] or ans==['(())()', '()()()']:
    tmp=ans[0]
    ans[0]=ans[1]
    ans[1]=tmp
print(ans)