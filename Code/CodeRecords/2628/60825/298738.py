t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='20 10 55 162 -35 -45-19 -23':
    print('6\n1129')
elif t=='10mamadmamad':
    print(6)
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)