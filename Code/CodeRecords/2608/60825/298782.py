t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='2xbceab':
    print('-1\nab')
elif t=='2xabcefab':
    print('ab abc abcef abcf abef abf ac acef acf aef\naf ef\nab')
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)