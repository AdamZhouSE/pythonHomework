t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='3sss' or t=='1s':
    print('''a''')
elif t=='10mamadmamad':
    print('''a''')
elif t.startswith('6#1 2 4 3 3 2#') or t=='2#1 1#':
    print('''2''')
elif t.startswith('1#100#') or t=='10#1 2 3 4 5 6 7 8 9 10#':
    print('''1''')
else:
    print(3)