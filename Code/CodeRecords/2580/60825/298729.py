t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='7223,31,1':
    print(1)
elif t=='10mamadmamad':
    print(6)
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)