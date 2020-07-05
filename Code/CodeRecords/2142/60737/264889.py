t = int(input())
while t:
    exp = list(input())
    ctl = 0
    ret = []
    stk = []
    for i in exp:
        if i == '(':
            ctl += 1
            ret.append(ctl)
            stk.append(ctl)
        elif i == ')':
            ret.append(stk.pop())
        else:
            continue
    for j in ret:
        print(j, end=" ")
    t -= 1
    print()
    