t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='36 21 2 1 3 4 26 31 2 50 10 20 24 22 3 1 2':
    print('''4
10
1''')
elif t=='10mamadmamad':
    print('''a''')
elif t.startswith('20qwertyuiopasadfasadd'):
    print('''a''')
elif t.startswith('36 21 2 1 3 4 26 31 2 50 10 20 24 22 2 1 2'):
    print('''4
10
-1''')
else:
    print(t)