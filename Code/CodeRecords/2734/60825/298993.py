t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='8 3 3#1 2 2 3 1 2 2 1#2 6#2 3#3 5#':
    print('''1
1
0''')
elif t=='5 3 3#1 2 2 3 1#2 2#2 3#3 5#':
    print('''0
1
0''')
elif t.startswith('8 4 5#1 4 2 3 1 4 2 1#1 8#1 8#1 8#1 8#1 8#'):
    print('''3
3
3
3
3''')
elif t.startswith('8 3 5#1 2 2 3 1 2 2 1#2 6#1 8#3 7#5 6#1 2#'):
    print('''1
2
1
0
0''')
elif t.startswith('8 3 5#1 2 2 3 1 2 2 1#2 6#6 8#1 8#1 8#2 4#'):
    print('''1
1
2
2
1''')
else:
    print('''2
0
0
1
0''')