x = int(input())
y = int(input())
neg = x < 0 and y >= 0 or x >= 0 and y < 0
if x < 0:
    x = -x
if y < 0:
    y = -y

result = 0
if x >= y:
    result += int(x/y)
    x = x%y

dec = ''
rest = {}
while x > 0:
    if str(x) in rest:
        start = rest[str(x)]
        dec = '.%s(%s)'%(dec[:start], dec[start:])
        break
    rest[str(x)] = len(dec)

    x *= 10
    dec += str(int(x/y))
    x %= y
else:
    if len(dec) > 0:
        dec = '.' + dec
result = str(result) + dec
print(result)