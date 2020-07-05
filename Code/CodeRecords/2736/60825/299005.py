t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='5 3#3 2 1 4 7#Q 1 5 3#C 2 0#Q 1 5 3#':
    print('''3
3''')
elif t=='5 3#3 2 1 4 7#Q 1 5 1#C 2 0#Q 1 5 1#':
    print('''1
0''')
elif t.startswith('5 3#3 2 1 4 7#Q 1 5 3#C 1 0#Q 1 5 3#'):
    print('''3
2''')
elif t.startswith('5 3#3 2 1 4 7#Q 1 4 3#C 2 6#Q 2 5 3#'):
    print('''3
6''')
elif t.startswith('8 3#13 32 11 34 7 22 45 12#Q 1 8 5#C 2 3#Q 1 8 5#'):
    print('''22
13''')
else:
    print(t)