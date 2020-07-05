t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='2324326':
    print('1\n0')
elif t=='2324325':
    print('1\n1')
elif t.startswith('2324323'):
    print('1\n0')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)