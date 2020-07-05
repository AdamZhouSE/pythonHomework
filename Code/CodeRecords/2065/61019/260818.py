s = input().strip()
head = ''
if s[0] == '+' or s[0] == '-':
    head = s[0]
    s = s[1:]
r = 0
for i in range(len(s)):
    if s[i].isnumeric():
        r *= 10
        r += eval(s[i])
    else:
        break
r = -r if head == '-' else r
if r < -2 ** 31:
    r = -2 ** 31
if r > 2 ** 31 - 1:
    r = 2 ** 31 - 1

print(r)
