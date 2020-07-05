def f(s):
    t = list(s)
    i = 0
    m = []
    n = []
    while i < len(t):
        if t[i] == ' ':
            pass

        elif '9' >= t[i] >= '0' :
            m.append(t[i])
        elif t[i]=='(':
            n.append('(')
        elif t[i] == '+' or t[i] == '-':
            if len(n) == 0:
                n.append(t[i])
            else:
                y=n.pop()
                if y == '+':
                    b = m.pop()
                    a = m.pop()
                    m.append(str(int(a) + int(b)))
                    i -= 1
                elif y == '-':
                    b = m.pop()
                    a = m.pop()
                    m.append(str(int(a) - int(b)))
                    i -= 1
                else:
                    n.append(t[i])
        else:
            x = n.pop()
            b = m.pop()
            a = m.pop()
           
            if x == '+':
                m.append(str(int(a) + int(b)))
            else:
                m.append(str(int(a) - int(b)))
        i += 1
    if n[0]=='+':
        return int(m[0])+int(m[1])
    else:
        return int(m[0])-int(m[1])


print(f(input().strip()))


