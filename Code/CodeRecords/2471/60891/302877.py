t = int(input())
ans_l = []
for i in range(t):
    s = input()
    exp_l = []
    is_b = True
    for j in range(len(s)):
        if s[j] == '{' or s[j] == '[' or s[j] == '(':
            exp_l.append(s[j])
        elif s[j] == '}' or s[j] == ']' or s[j] == ')':
            t = exp_l.pop()
            if (t == '{' and s[j] != '}') or (t == '[' and s[j] != ']') or (t == '(' and s[j] != ')'):
                is_b = False
                break
    if len(exp_l) > 0:
        is_b = False
    if is_b:
        ans_l.append('balanced')
    else:
        ans_l.append('not balanced')
for i in ans_l:
    print(i)
