s = input()

try:
    while True:
        target = input()
        t = s.upper()
        u = s.lower()
        new1 = target.replace(t, '')
        new2 = new1.replace(u, '')
        print(new2.replace(' ', ''))
except EOFError:
    pass