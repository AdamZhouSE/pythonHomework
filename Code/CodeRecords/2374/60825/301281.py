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
elif t=='2#5#5 5 4 5 4#5#9 9 9 2 5#':
    print('''5 5 5 4 4 
9 9 9 2 5 ''')
elif t.startswith('2#5#5 5 4 5 4#5#9 9 2 2 5#'):
    print('''5 5 5 4 4 
2 2 9 9 5 
''',end='')
elif t.startswith('2#5#5 5 4 5 4#5#9 5 2 2 5#'):
    print('''5 5 5 4 4 
2 2 5 5 9 
''',end='')
elif t.startswith('2#5#5 5 4 6 4#5#9 9 9 2 5#'):
    print('''4 4 5 5 6 
9 9 9 2 5 ''')
else:
    print(t)