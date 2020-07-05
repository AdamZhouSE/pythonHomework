def my_eval(s):
    s = s.replace(' ', '')
    tr = list(trans(s))
    ans = []
    for i in range(len(tr)):
        ch = tr[i]
        if ch.isdigit():
            ans.append(int(ch))
        else:
            ans.append(cal(ch, ans.pop(), ans.pop()))
    return ans.pop()


def cal(op, a, b):
    if op == '+':
        return str(int(a) + int(b))
    else:
        return str(int(b) - int(a))


def trans(s):
    strlist = list(s)
    lens = len(strlist)
    out = ''
    temp = []
    for i in range(lens):
        ch = strlist[i]
        if ch == ' ':
            continue
        elif ch.isdigit():
            out += ch
            continue
        elif ch == '(':
            temp.append(ch)
            continue
        elif ch == '+' or ch == '-':
            while temp and temp[-1] != '(':
                out += temp.pop()
            temp.append(ch)
            continue
        elif ch == ')':
            while len(temp) and temp[-1] != '(':
                out += temp.pop()
            temp.pop()
            continue
    while len(temp):
        out += temp.pop()
    return out


if __name__ == "__main__":
    s = input()
    print(my_eval(s))
