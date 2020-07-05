def f(a, b):
    s = ""
    if a[0]=="D":
        s = delete(a[1], b)
    elif a[0]=="I":
        s = insert(a[1], a[2], b)
    elif a[0]=="R":
        s = replace(a[1], a[2], b)
    return s


def delete(a, x):
    n = -1
    for i in range(len(x)):
        if x[i] == a:
            n = i
            break
    if n == len(x)-1:
        x = x[:n]
    elif n == -1:
        print("no exist")
    else:
        x = x[:n]+x[n+1:]
    return x


def insert(a1, a2, b):
    last = -1
    for i in range(len(b)):
        if b[i] == a1:
            last = i
    if last == -1:
        print("no exist")
        return b
    return b[:last]+a2+b[last:]


def replace(a1, a2, b):
    c = b.replace(a1, a2)
    if b == c:
        print("no exist")
    return c


s = input()
func = input().replace(" ", "")
s = f(func, s)
print(s)