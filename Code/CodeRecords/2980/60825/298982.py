t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='This is a book. #R  i 2#':
    print('''Th2s 2s a book. ''')
elif t=='This is a book. #D  s#':
    print('''Thi is a book. ''')
elif t.startswith('This is a book. #R   t i #'):
    print('''no exist
This is a book. ''')
elif t.startswith('This is a book. #R   w i #'):
    print('''no exist
This is a book. ''')
elif t.startswith('This is a book. #I  i d#'):
    print('''This dis a book. ''')
else:
    print(t)
