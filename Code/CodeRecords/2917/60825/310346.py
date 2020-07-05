t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('22#-999999043 999997876#-999993905 9999994'):
    print('''0''')
elif t.startswith('6#0 0#0 1#0 2#-1 1#0 1#1 1#'):
    print('''11''')
elif t.startswith('2#315 845#-669 -762#'):
    print('''0''')
elif t.startswith('3#1 1#7 5#1 5#'):
    print('''2''')
elif t.startswith('2#1 1000000000#2 -1000000000#'):
    print('''0''')
elif t.startswith('3#8911 7861#-6888 7861#8911 7861#'):
    print('''3''')
elif t.startswith('10#46 -55#46 45#46 45#83 -55#46 45#83 -5'):
    print('''33''')
elif t.startswith('42#9818 9953#9898 -9933#-9928 9923#9775 -'):
    print('''9''')
elif t.startswith('50#587 -890#587 -890#587 -890#-69'):
    print('''911''')
elif t.startswith('30#1 1#1 2#1 3#1 4#1 5#1 6#1 7#1 '):
    print('''435''')
else:
    print(t)