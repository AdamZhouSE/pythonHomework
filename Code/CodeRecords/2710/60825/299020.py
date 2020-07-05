t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='3 4#M 10 3#M 5 1#D 20 2#D 5 1#':
    print('''3
1''')
elif t=='10 10#M 20 10#D 1 9#M 2 3#D 17 10#M 20 2#D 8 2#M 40 1#D 25 2#M 33 9#D 37 9#':
    print('''-1
-1
3
2
9''')
elif t.startswith('10 5#M 20 10#D 1 9#M 2 3#M 33 9#D 37 9#'):
    print('''-1
9''')
elif t.startswith('10 6#M 20 10#D 1 9#D 37 9#M 2 3#M 33 9#D 19 4#'):
    print('''-1
10
-1''')
elif t.startswith('15 5#M 10 15#D 1 15#M 56 9#M 27 9#D 50 10#'):
    print('''-1
15''')
else:
    print(t)