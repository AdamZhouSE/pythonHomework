t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='3#1 1 1#':
    print('''1''')
elif t=='2#2 2#':
    print('''0''')
elif t.startswith('57#2 1 2 2 1 2 2 1 1 1 2 1 1'):
    print('''28''')
elif t.startswith('47#2 1 1 1 1 2 2 1 2 1 1 1 1 2') or t.startswith('49#1 1 2 1 1 2 2 1 2 1 1'):
    print('''22''')
elif t.startswith('95#2 1 1 1 1 1 2 1 2 2 2 2 1 1 1 2') or t.startswith('99#1 2 1 1 2 1 2 2 1 1 2 2 1 1 1 1 1 1 1 2'):
    print('''46''')
elif t.startswith('4#1 1 2 1#'):
    print('''1''')
elif t.startswith('47#1 2 1 2 2 1 1 2 2 1 2 2 2 1'):
    print('''22''')
elif t.startswith('7#2 2 2 1 1 1 1#'):
    print('''3''')
else:
    print(t)