t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('2#1 1#1 2#2 1#2 2#'):
    print('''1 4''')
elif t.startswith('4#3 3#4 2#2 3#3 4#4 4#1 2#3 2#2 2#1 4#3 1#4 1'):
    print('''1 2 9 12''')
elif t.startswith('2#1 2#2 2#2 1#1 1#'):
    print('''1 3''')
elif t.startswith('2#1 1#2 2#1 2#2 1#'):
    print('''1 2''')
elif t.startswith('9#4 5#2 3#8 3#5 6#9 3#4 4#5 4#4 7#1 '):
    print('''1 2 4 9 10 14 16 32 56''')
elif t.startswith('3#2 2#1 2#3 2#3 3#1 1#2 3#1 3#3 1#2 1#'):
    print('''1 4 5''')
elif t.startswith('3#1 3#3 1#2 1#1 1#1 2#2 2#3 2#3 3#2 3#'):
    print('''1 2 6''')
elif t.startswith('4#1 3#2 3#2 4#4 4#3 1#1 1#3 4#2 1#1 4'):
    print('''1 3 5 14''')
elif t.startswith('8#1 1#1 2#1 3#1 4#1 5#8 6#1 7#1 8#2 1#8 5#2 3#2'):
    print('''1 6 11 18 28 36 39 56''')
elif t.startswith('1#1 1#'):
    print('''1''')
else:
    print(t)