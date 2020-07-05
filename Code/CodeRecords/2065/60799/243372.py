s = input().strip(' ')
p = ''
if s[0:1] == '-':
    s = s[1:]
    p = '-'
i = 0
while i < len(s):
    if s[i].isdigit():
        i += 1
    else:
        break
s = p + s[0:i]
if s == '':
    s = '0'
s = int(s)
s = max(s, -2147483648)
s = min(s, 2147483647)
print(s)