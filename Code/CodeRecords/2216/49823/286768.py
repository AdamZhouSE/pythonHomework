def bi(expression):
    def gcd(a, b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    def lcm(*args):
        l=1
        for i in args:
            if l%i!=0:
                l*=(i//gcd(l,i))
        return l

    E = [tuple(e.split('/')) for e in expression.replace('-', '+-').strip('+').split('+')]
    numerators = (int(i[0]) for i in E)
    denominators = [int(i[1]) for i in E]
    D = lcm(*{i for i in denominators})
    N = sum(n * f for n, f in zip(numerators, [D // i for i in denominators]))
    g = gcd(abs(N), D)
    print(f'{N // g}/{D // g}')
if __name__ == '__main__':
    bi(input())
