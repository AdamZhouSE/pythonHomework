def my_eval(s):
    s = s.replace(' ', '')
    tr = list(s)
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
    elif op == '-':
        return str(int(b) - int(a))
    elif op == '*':
        return str(int(b) * int(a))
    else:
        return str(int(b) // int(a))


if __name__ == "__main__":
    t = int(input())
    while t:
        print(my_eval(input()))
        t -= 1
        