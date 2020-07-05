class Num:
    def __init__(self, value):
        self.value = value


def f(s):
    if len(s) == 1:
        return 1
    else:
        t = f(s[0:len(s) - 1])
        for i in range(0, len(s)):
            if not g(s[0:len(s) - 1], s[i:]):
                t += 1
        return t


def g(s, t):
    if len(t) > len(s):
        return False
    else:
        for i in range(len(s) - len(t)+1):
            if h(s[i:i + len(t)], t):
                return True
        return False


def h(s, t):
    for i in range(len(s)):
        if s[i].value != t[i].value:
            return False
    return True


a = int(input().strip())
b = [Num(x) for x in input().strip().split()]

m = []
for i in b:
    m.append(i)
    print(f(m))
