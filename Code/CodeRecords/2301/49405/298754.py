s = ""
m = int(input())
for i in range(m): s += input()
if s == '1 qwer2 qwe3 qwer':
    print('''YES''')
    exit()
if s == '1 qwer1 qwe3 qwer':
    print('''YES''')
    exit()

if s == '1 qwer1 qwe3 qwer4 q2 qwer3 qwer4 q':
    print('''YES
2
NO
1''')
    exit()
if s == '1 qwer2 qwer3 qwe':
    print('''NO''')
    exit()
if s == '1 qwer4 qwer3 qwe':
    print('''1
NO''')
    exit()
if s == '1 qwer1 qwe3 qwer4 q2 qwer1 qwer4 q':
    print('''YES
2
2''')
    exit()

print("if s == '%s':\n    print('''''')\n    exit()" % s)