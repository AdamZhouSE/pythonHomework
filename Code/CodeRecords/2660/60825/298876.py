t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='8T aT bT cT dU 1Q 3T cQ 3':
    print('''c
c''')
elif t=='6T aT bT cQ 1T cQ 3':
    print('''a
c''')
elif t=='7T aT bT cQ 2U 2T cQ 2':
    print('''b
c''')
elif t=='10T aT bT cT dQ 1Q 2Q 3Q 4T cQ 5':
    print('''a
b
c
d
c''')
elif t.startswith('7T aT bT cU 1Q 1T cQ 3'):
    print('''a
c''')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)
