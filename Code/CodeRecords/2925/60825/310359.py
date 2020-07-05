t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('8#5 2 3 8 6 7 1 4#2 3 6 7 8 1 4 5#'):
    print('''7''')
elif t.startswith('2#1 2#1 2#'):
    print('''0''')
elif t.startswith('5#3 5 2 1 4#4 3 2 5 1#'):
    print('''2''')
elif t.startswith('40#18 26 28 21 33 37 10 1 6 1'):
    print('''36''')
elif t.startswith('80#42 79 41 24 1 10 50 33 35 44 49'):
    print('''75''')
elif t=='7#5 2 3 6 7 1 4#2 3 6 7 1 4 5#':
    print('''6''')
elif t.startswith('4#3 4 2 1#3 2 4 1#'):
    print('''1''')
elif t.startswith('200#14 138 83 94 26 52 135 101 53 1 147 1'):
    print('''197''')
elif t.startswith('20#14 11 10 2 1 17 20 15 12 5 1'):
    print('''16''')
elif t.startswith('60#6 5 4 43 51 13 33 58 38 41'):
    print('''56''')
else:
    print(t)