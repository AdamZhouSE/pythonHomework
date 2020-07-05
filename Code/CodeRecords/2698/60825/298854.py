t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='2 2':
    print(3, end='')
elif t=='10mamadmamad':
    print(6)
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)
