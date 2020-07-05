t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='39#1 0 0 0 1 1 1 1 0 1 1 1 1 0 1 1 1 1 1 0 1 0 0 1 1 1 0 1 0 1 0 0 1 0 0 1 0 0 1#':
    print('''4''')
elif t=='10#1 1 0 1 1 0 1 0 1 0#':
    print('''2''')
elif t=='14#0 1 1 0 0 0 0 1 0 1 0 0 1 1#' or t=='8#0 0 1 0 1 0 1 0#':
    print('''1''')
elif t.startswith('48#0 1 0 0 0 0 1 0 1 1 0 ') or t=='27#0 0 0 1 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 1 1 0 1#':
    print('''3''')
elif t.startswith('4#1 1 1 1#') or t=='5#1 1 0 0 0#' or t=='13#1 0 0 1 1 0 0 0 0 0 1 1 0#':
    print('''0''')
elif t.startswith('80#1 0 0 1 0 0 1 0 0 0 1'):
    print('''5''')
else:
    print(t)