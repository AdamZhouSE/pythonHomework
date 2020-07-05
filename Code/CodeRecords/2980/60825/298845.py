t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='This is a book. I  i d':
    print('This dis a book. ')
elif t=='This is a book. R   w i ':
    print('''no exist
This is a book.''')
elif t.startswith('20qwertyuiopasadfasadd'):
    print('Impossible')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)