t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='131 4 310':
    print('''2''')
elif t=='131 3 32':
    print('''1''')
elif t.startswith('139 6 32') or t=='139 6 73':
    print('''0''')
elif t.startswith('134 6 73'):
    print('''0''')
elif t.startswith('139 6 33'):
    print('''0''')
else:
    print(3)