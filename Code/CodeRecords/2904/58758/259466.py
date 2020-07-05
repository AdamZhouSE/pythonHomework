n = input()
isNeg = False
if n[0] == '-':
    isNeg = True
    n = n[1:]
ans = ''
for ch in n:
    ans = ch+ans
if ans[0] == '0' and len(ans) != 1:
    while ans[0] == '0':
        ans = ans[1:]
if isNeg:
    ans = '-'+ans
print(ans)
