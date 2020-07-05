n = eval(input())
res = []
while n > 0:
    n -= 1
    r = n % 26
    res.append(r)
    n //= 26
print(''.join([chr(i + ord('A')) for i in res[::-1]]))
