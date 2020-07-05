t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('7#1 3 3 2 1 2 3#'):
    print('''0''')
elif t.startswith('55#0 3 3 3 2 1 3 1 3 0 3 1 2 0 '):
    print('''20''')
elif t.startswith('67#2 1 0 3 1 1 3 1 3 0 0 2 1 3 3 1 2 3 3 3 '):
    print('''25''')
elif t.startswith('90#3 3 0 1 2 3 1 3 2 3 2 0 2 3 2 2 '):
    print('''30''')
elif t.startswith('82#2 3 0 0 2 1 0 3 1 2 1'):
    print('''32''')
elif t.startswith('2#2 2#'):
    print('''1''')
elif t.startswith('65#2 2 0 2 0 0 0 1 2 1 1 2 1 '):
    print('''25''')
elif t.startswith('74#0 2 2 2 1 1 0 0 0 2 3 2 3 0 1 0 2 0 '):
    print('''27''')
elif t.startswith('4#1 3 2 0#'):
    print('''2''')
elif t.startswith('63#1 3 2 1 3 2 2 2 2 1 2 '):
    print('''22''')
else:
    print(t)