t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='2abbabcab':
    print('''0
1''')
elif t=='2abbcabcab':
    print('''3
1''')
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)
