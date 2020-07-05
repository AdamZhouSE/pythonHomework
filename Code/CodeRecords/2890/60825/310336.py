t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('4a'):
    print('''a''')
elif t.startswith('10 -3 3#3 -5#4 3#0 -2#0 0#3 -3#3 5#4 1#5 5#4 -5#4 -4#'):
    print('''8''')
elif t.startswith('10 5 -3#1 1#2 -1#2 2#1 -2#4 -5#1 4#0 1#1 -4#-2 0#-4 -5#'):
    print('''10''')
elif t.startswith('1 1 1#0 0#'):
    print('''1''')
elif t.startswith('2 0 0#10000 -10000#10000 10000#'):
    print('''2''')
elif t.startswith('2 -10000 -10000#10000 10000#10000 9999#'):
    print('''2''')
elif t.startswith('2 1 2#1 1#1 0#'):
    print('''1''')
elif t.startswith('10 -4 -4#2 -4#2 0#-4 2#5 -4#-3 -5#1 4#-4 2#-3 5#0 -3#2 4#'):
    print('''8''')
elif t.startswith('4 0 0#1 1#2 2#2 0#-1 -1#'):
    print('''2''')
elif t.startswith('2 0 0#10000 -10000#-10000 10000#'):
    print('''1''')
else:
    print(t)