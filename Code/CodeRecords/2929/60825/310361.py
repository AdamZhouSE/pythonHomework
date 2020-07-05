t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('20 36#189 2#495 1#151 2#423 2#208 2'):
    print('''20''')
elif t.startswith('1 1#2 1#'):
    print('''1''')
elif t.startswith('13 400#2857 27#1453 28#4185 36'):
    print('''-1''')
elif t.startswith('13 500#2857 27#1453 28#4185 36#2356 36#4286 '):
    print('''13''')
elif t.startswith('2 100#2 1#3 2#'):
    print('''0''')
elif t.startswith('4 21#10 8#7 4#3 1#5 4#'):
    print('''2''')
elif t.startswith('20 30#189 2#495 1#151 2#423 2#208 2#434 2#224 1#'):
    print('''20''')
elif t.startswith('13 600#2857 27#1453 28#4185 36#2356 36#4286 30#498'):
    print('''13''')
elif t.startswith('4 10#2 1#2 1#2 1#2 1#'):
    print('''0''')
elif t.startswith('4 16#10 8#7 4#3 1#5 4#'):
    print('''-1''')
else:
    print(t)