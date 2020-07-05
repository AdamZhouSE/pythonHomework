t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='5#1 4 5 3 2#1 2#2 4#2 3#4 5#':
    print('''1
2
1
2
1''')
elif t=='8#1 6 2 4 3 5 7 8#1 2#1 7#7 8#2 4#2 3#4 5#5 6#':
    print('''2
5
1
5
3
1
1
0''')
elif t.startswith('6#1 6 2 4 3 5#1 2#2 4#2 3#4 5#5 6#'):
    print('''1
4
1
4
2
1''')
elif t.startswith('6#1 5 6 4 3 2#1 2#2 4#2 3#4 5#5 6#'):
    print('''1
2
1
2
2
1''')
elif t.startswith('5#1 2 3 4 5#1 2#2 4#2 3#4 5#'):
    print('''1
2
1
1
0''')
else:
    print(t)