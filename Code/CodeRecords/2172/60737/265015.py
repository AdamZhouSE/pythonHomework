def trans(s):
    strlist = list(s)
    lens = len(strlist)
    out = ''
    temp = []
    for i in range(lens):
        ch = strlist[i]
        if ch == ' ':
            continue        
        elif ch == '(':
            temp.append(ch)
            continue
        elif ch == '+' or ch == '-':
            while temp and temp[-1] != '(':
                out += temp.pop()
            temp.append(ch)
            continue
        elif ch == '*' or ch == '/':
            while temp and (temp[-1] == '*' or temp[-1] == '/'):
                out += temp.pop()
            temp.append(ch)
            continue
        elif ch == '^':
            while temp and temp[-1] == '^':
                out += temp.pop()
            temp.append(ch)
            continue
        elif ch == ')':
            while len(temp) and temp[-1] != '(':
                out += temp.pop()
            temp.pop()
            continue
        else:
            out += ch
            continue
    while len(temp):
        out += temp.pop()
    return out


if __name__ == "__main__":
    t = int(input())
    while t:
        s = input()
        print(trans(s))
        t -= 1
