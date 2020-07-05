s = input()
head = ''
if s[0] == '+' or s[0] == '-':
    head = s[0]
    s = s[1:]
s=s[::-1]
while s[0]=='0':
    s=s[1:]
print(head + s)
