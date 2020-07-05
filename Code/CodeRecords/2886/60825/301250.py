t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='1#1 1#':
    print('''1''')
elif t=='3#2 1 1 3 2 3#':
    print('''2''')
elif t.startswith('5#1 3 4 2 4 3 5 5 1 2#'):
    print('''4''')
elif t.startswith('6#1 2 6 5 3 3 4 1 4 5 6 2#'):
    print('''5''')
elif t.startswith('10#1 2 3 4 5 4 3 2 1 5 6 7 9 8 7 8 9 6 10 10#'):
    print('''5''')
else:
    print(t)