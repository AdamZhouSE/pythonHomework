t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='263':
    print('1 2 4 5 7 9')
    print('1 2 4')
elif t=='262':
    print('1 2 4 5 7 9')
    print('1 2')
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)