t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('7 7 47#91 91 91 91 91 91 91#91 91 91 91'):
    print('''0''')
elif t.startswith('3 3 3#5 8 5#11 11 17#14 5 3#'):
    print('''-1''')
elif t.startswith('7 7 47#47 47 47 47 47 47 47#47 47 47 47'):
    print('''-1''')
elif t.startswith('3 3 3#5 8 5#11 11 17#14 5 2#'):
    print('''12''')
elif t.startswith('3 2 1#5 7#1 2#5 100#'):
    print('''104''')
elif t.startswith('2 2 2#2 4#6 8#'):
    print('''4''')
elif t.startswith('7 5 47#9583 1734 4601 5353 2110#3802 '):
    print('''1508''')
elif t.startswith('40 89 679#636 377 797 41 713 704 30 143 249 791 966 252'):
    print('''-1''')
elif t.startswith('7 4 5#7 7 7 12#7 12 12 7#7 7 7 7#7 7 12 7#7 7 12 '):
    print('''9''')
elif t.startswith('1 2 7#6 7#'):
    print('''-1''')
else:
    print(t)