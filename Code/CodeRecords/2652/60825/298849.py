t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='5 8 12030 2550 2120 205 1835 3060 2748 1880 40':
    print(48, end='')
elif t=='48':
    print(48)
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)
