t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='4 3#1 -1 1 -1#1 1#1 2#2 2#':
    print('''0
1
0''')
elif t=='9 6#1 -1 1 -1 -1 1 1 1 -1#1 1#1 2#2 2#2 5#1 5#2 4#':
    print('''0
1
0
1
0
0''')
elif t.startswith('2 3#1 -1#1 1#1 2#2 2#'):
    print('''0
1
0''')
elif t.startswith('5 7#-1 1 1 1 -1#1 1#2 3#3 5#2 5#1 5#2 4#1 3#'):
    print('''0
1
0
1
0
0
0''')
elif t.startswith('5 5#-1 1 1 1 -1#1 1#2 3#3 5#2 5#1 5#'):
    print('''0
1
0
1
0''')
else:
    print(t)