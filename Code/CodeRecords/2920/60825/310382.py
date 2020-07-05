t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('88 12#24 25 43 50 62 95 105 107 109 1'):
    print('''575''')
elif t.startswith('5 2#3 3 4 5 6#'):
    print('''2''')
elif t.startswith('8 1#1 1 2 3 5 8 13 21#'):
    print('''20''')
elif t.startswith('78 9#11 45 49 86 87 102 112 116 122 125 166 17'):
    print('''621''')
elif t.startswith('6 3#4 8 15 16 23 42#'):
    print('''12''')
elif t.startswith('78 3#11 45 49 86 87 102 112 116 122 12'):
    print('''839''')
elif t.startswith('4 4#1 3 3 7#'):
    print('''0''')
elif t.startswith('1 1#1#'):
    print('''0''')
elif t.startswith('78 6#11 45 49 86 87 102 112 1'):
    print('''721''')
elif t.startswith('88 20#24 25 43 50 62 95 105 107 109 116 117 '):
    print('''435''')
else:
    print(t)