read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    a = read()
    b = read()
    inte = str(a // b)
    a %= b
    done = []
    if not a:
        print(inte)
        continue
    while a:
        a *= 10
        r = a // b
        if r in done:
            loc = done.index(r)
            bef = done[:loc]
            aft = done[loc:]
            print(inte + '.' +
                  ''.join([str(x) for x in bef]) + '(' +
                  ''.join([str(x) for x in aft]) + ')')
            break
        done.append(r)
        a %= b
    else:
        print(inte + '.' + ''.join([str(x) for x in done]))
