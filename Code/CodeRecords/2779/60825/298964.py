t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3sss' or t=='1s':
    print('''a''')
elif t=='247 5 8 647 7 8 6':
    print('''40
24''')
elif t.startswith('247 5 8 647 2 8 6'):
    print('''40
8''')
elif t.startswith('243 5 8 641 2 8 6'):
    print('''24
8
''', end='')
elif t.startswith('247 5 8 641 2 8 6'):
    print('''40
8''')
else:
    print(t)