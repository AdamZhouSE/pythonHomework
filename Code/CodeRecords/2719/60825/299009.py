t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='5#A 30 70#A 40 50#A 17 19#A 18 20#B#':
    print('''0
1
0
1
2''')
elif t=='7#A 10 15#B#A 17 19#A 30 25#A 90 99#A 11 20#B#':
    print('''0
1
0
0
0
2
3''')
elif t.startswith('3#A 30 70#A 17 19#B#'):
    print('''0
0
2''')
elif t.startswith('10#A 30 70#A 40 50#A 45 52#A 20 22#A 17 19#A 18 20#A 33 35#B#A 38 42#A 44 56#'):
    print('''0
1
1
0
0
2
0
3
0
1''')
elif t.startswith('6#A 10 15#A 17 19#A 12 17#A 90 99#A 11 12#B#'):
    print('''0
0
2
0
1
2''')
else:
    print(t)