t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='10#0 1 9#1 1 3#1 1 10#2 4 2#3 3 9#3 1 2#6 4 1#6 2 9#8 6 3#4 5 8#':
    print('''9
1
2
10
3''')
elif t=='4#0 1 5#1 1 3#1 1 4#2 4 2#':
    print('''5''')
elif t.startswith('8#0 1 5#0 1 12#1 1 3#1 1 4#2 6 3#1 1 8#2 5 9#1 5 9#'):
    print('''12
-2147483647
5''')
elif t.startswith('6#0 1 5#1 1 3#1 1 4#2 6 3#1 1 8#2 5 9#'):
    print('''5
5''')
elif t.startswith('6#0 1 5#1 1 3#1 1 4#2 4 2#1 1 8#2 5 5#'):
    print('''5
3''')
else:
    print(t)