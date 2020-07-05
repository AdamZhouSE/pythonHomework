s = list(input())
m = []
for i in range(len(s)):
    if s[i] == "(":
        m.append("(")
    elif s[i] == ")":
        m.pop()
    else:
        continue
if m == []:
    print("YES")
else:
    print("NO")
