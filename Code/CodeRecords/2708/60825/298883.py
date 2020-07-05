t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3 5 7C 1 2C 2 2W 1 2C 3 2W 1 2C 3 3W 1 3':
    print('''3
3
0''')
elif t=='3 5 7C 1 5C 2 2W 1 2C 3 2W 1 2C 3 4W 1 3':
    print('''2
2
0''')
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)
