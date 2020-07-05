x = eval(input())
y = eval(input())
res = []
have = [0] * 10
loop = -1
while x < y:
    x *= 10
    res.append(0)

while True:
    r = x // y
    if r != 0 and res.count(r) > 0:
        loop = res.index(r)
        break
    res.append(r)

    x = x % y
    if x == 0:
        break
    x *= 10

op = ''
op += str(res[0])
if len(res) > 1:
    op += '.' + ''.join([str(r) for r in res[1:loop]])
    if loop != -1:
        op += '('
    op += ''.join([str(r) for r in res[loop:]])
    if loop != -1:
        op += ')'

print(op)