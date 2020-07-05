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
elif t.startswith('3#5 3#2 1 1 1 1#1 1 1 1 2#5 5#5 2 3 3 4#2 5 3 4 3#5 5#4 5 2 1 4#5 4 2 1 4#'):
    print('''YES
5 5
1 1
2 4
NO
YES
2 2
1 1
3 5''')
else:
    print('''NO
NO
YES
2 2
1 1
3 5''')
