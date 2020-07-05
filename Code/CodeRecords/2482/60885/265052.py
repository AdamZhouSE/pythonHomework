def find_rest(rest, D):
    if rest == 0:
        return ''
    quotient = ''
    recent = []
    while rest > 0:
        recent.append(rest)
        rest *= 10

        q = int(rest/D)
        rest = rest % D
        quotient += str(q)
        if rest in recent:
            index = recent.index(rest)
            return '.%s(%s)'%(quotient[:index], quotient[index:])
    return '.%s'%quotient

def test():
    N = int(input())
    D = int(input())
    integer = str(int(N/D))
    N = N % D
    rest = find_rest(N, D)
    ans = integer + rest
    A.append(ans)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)