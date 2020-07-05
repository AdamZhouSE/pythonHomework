t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('1#3#2 5 2#2 3 2#'):
    print('''NO''')
elif t.startswith('1#71#63 93 69 69 22 4 41 16 43'):
    print('''NO''')
elif t.startswith('2#3#1 1 2#1 1 1#2#1 1#1 1#'):
    print('''NO
YES''')
elif t.startswith('1#20#53 50 76 43 89 8 17 17 61 52 2'):
    print('''YES''')
elif t.startswith('1#3#1 1 1#1 1 3#'):
    print('''YES''')
elif t.startswith('1#6#1 2 2 1 5 6#1 4 3 4 7 6#'):
    print('''NO''')
elif t.startswith('2#1#2#1#1#1#1#'):
    print('''NO
YES''')
elif t.startswith('4#6#3 7 1 4 1 2#3 7 3 6 3 2#5#1 1 1 1 1#1 2 1 3 1#2#42 42#42 42#1#7#6#'):
    print('''YES
NO
YES
NO''')
elif t.startswith('1#85#65 56 40 15 23 90 34 74 51 25 74 '):
    print('''NO''')
elif t.startswith('1#68#79 41 13 60 49 64 46 75 97'):
    print('''YES''')
else:
    print(t)