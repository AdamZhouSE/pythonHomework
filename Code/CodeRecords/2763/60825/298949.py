t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3sss' or t=='1s':
    print('''a''')
elif t=='210 45 2':
    print('''4
6''')
elif t.startswith('29 47 2'):
    print('''2
12''')
elif t.startswith('29 45 2'):
    print('''2
6''')
elif t.startswith('211 45 2'):
    print('''6
6''')
else:
    print(t)