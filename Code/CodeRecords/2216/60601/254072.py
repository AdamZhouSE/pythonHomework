def solve(expression:str):
    i = 0
    a, b, c, d = '', '', '', ''
    while expression[i] != '/':
        a += expression[i]
        i += 1
    i += 1
    while i < len(expression) and expression[i] not in ['+', '-']:
        b += expression[i]
        i += 1
    a, b = int(a), int(b)
    while i < len(expression):
        while expression[i] != '/':
            c += expression[i]
            i += 1
        i += 1
        while i < len(expression) and expression[i] not in ['+', '-']:
            d += expression[i]
            i += 1
        c, d = int(c), int(d)
        a, b = a * d + c * b, b * d
        c, d = '', ''

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    x = gcd(a, b)
    return str(a // x) + '/' + str(b // x)

print(solve(input()))