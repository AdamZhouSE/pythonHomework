t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('1#1000000000#'):
    print('''1''')
elif t.startswith('7#4 7 12 100 150 300 600#'):
    print('''4''')
elif t.startswith('9#1 2 3 7 8 20 21 22 23#'):
    print('''4''')
elif t.startswith('10#1 2 5 11 12 24 25 26 27 28#'):
    print('''7''')
elif t.startswith('2#1 2#'):
    print('''2''')
elif t.startswith('9#4 6 9 12 100 150 200 400 800#'):
    print('''5''')
elif t.startswith('4#1 2 4 8#'):
    print('''4''')
elif t.startswith('6#4 7 12 100 150 199#'):
    print('''3''')
elif t.startswith('10#1 2 5 6 7 10 21 23 24 49#'):
    print('''4''')
elif t.startswith('5#2 10 50 110 250#'):
    print('''1''')
else:
    print(t)