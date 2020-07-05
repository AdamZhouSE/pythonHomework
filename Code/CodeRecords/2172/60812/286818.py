def icp(c):
    if c == '+' or c == '-':
        return 2
    elif c == '*' or c == '/':
        return 4
    elif c == '(':
        return 8
    elif c == ')':
        return 1
    else:
        return 7


def isp(c):
    if c == '+' or c == '-':
        return 3
    elif c == '*' or c == '/':
        return 5
    elif c == '(':
        return 1
    elif c == '^':
        return 6
    else:
        return 0


T = int(input())
for i in range(T):
    s, t = ['#'], input()
    i, tlen = 0, len(t)
    while i != tlen:
        if t[i].isalpha():
            print(t[i], end='')
        else:
            temp = s[len(s)-1]
            if icp(t[i]) > isp(temp):
                s.append(t[i])
            elif icp(t[i]) < isp(temp):
                print(s.pop(), end='')
                i -= 1
            else:
                s.pop()
        i += 1
    temp = s.pop()
    while temp != '#':
        print(temp, end='')
        temp = s.pop()
    print()