def pow(x,n):
    sign = True
    if n < 0:
        n *= -1
        sign = False
    result = 1.0
    for i in range(n):
        result *= x
    if not sign:
        result = 1/result
    return result

#main-----
base = float(input())
e = int(input())

print('%.5f'%pow(base,e))