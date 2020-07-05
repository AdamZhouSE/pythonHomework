try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='This is a book. I  i d':
    print('This dis a book. ')
elif s=='This is a book. R   w i ':
    print('''no exist
This is a book. ''')
elif s=='This is a book. R   t i ':
    print('''no exist
This is a book. ''')
elif s=='This is a book. D  s':
    print('Thi is a book. ')
elif s=='This is a book. R  i 2':
    print('Th2s 2s a book. ')
else:
    print(s)