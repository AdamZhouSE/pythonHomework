s = input()
p = ''
if '-' in s:
    p = '-'
    s = s[1:]
s = s[::-1].lstrip('0')
if s == '':
    s = '0'
print(p+s)