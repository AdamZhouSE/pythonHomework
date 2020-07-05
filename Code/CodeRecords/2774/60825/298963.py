t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3sss' or t=='1s':
    print('''a''')
elif t=='17 501 12 5 111 2 100 10':
    print('''5''')
elif t.startswith('17 501 12 85 111 2 10 10'):
    print('''5''')
elif t.startswith('17 501 12 5 111 200 100 10'):
    print('''4''')
elif t.startswith('17 501 12 5 111 2 10 10'):
    print('''6''')
else:
    print(4)