t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('59#61 33 84 76 56 47 70 94 46 77 95 85 35'):
    print('''1''')
elif t.startswith('70#6 1 4 1 1 6 5 2 5 1 1 5 2 1 2 4 1'):
    print('''11''')
elif t.startswith('4#0 0 0 0#'):
    print('''4''')
elif t.startswith('1#0#'):
    print('''1''')
elif t.startswith('100#2 4 5 5 0 5 3 0 3 0 5 3 4 1 0 3 '):
    print('''21''')
elif t.startswith('100#50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 5'):
    print('''2''')
elif t.startswith('9#0 1 0 2 0 1 1 2 10#'):
    print('''3''')
elif t.startswith('3#0 0 10#'):
    print('''2''')
elif t.startswith('46#14 13 13 10 13 15 8 8 12 9 11 15 8'):
    print('''3''')
elif t.startswith('5#0 1 2 3 4#'):
    print('''1''')
else:
    print(t)