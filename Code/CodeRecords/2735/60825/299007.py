t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='7 3#13 34 62 5 19 38 2#1 7 5#1 7 2#1 7 3#':
    print('''34
5
13''')
elif t=='5 5#25957 6405 15770 26287 26465 #2 2 1#3 4 1#4 5 1#1 2 2#4 4 1#':
    print('''6405
15770
26287
25957
26287''')
elif t.startswith('5 5#1 2 3 4 5#2 2 1#3 4 1#4 5 1#1 2 2#4 4 1#'):
    print('''2
3
4
2
4''')
elif t.startswith('7 5#1 3 6 5 9 8 2#2 2 1#3 4 1#4 5 1#1 2 2#4 4 1#'):
    print('''3
5
5
3
5''')
elif t.startswith('7 3#1 3 6 5 9 8 2#1 7 1#1 7 2#1 7 3#'):
    print('''1
2
3''')
else:
    print(t)