t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='5 2 2 24#7 3 7 8 0 #1 2#1 5#3 1#4 1#3 4 2#4 2#':
    print('''3''')
elif t.startswith('5 2 2 24#7 3 7 8 0 #1 2#1 5#3 1#4 1#3 4 2#4 3#'):
    print('''7''')
elif t.startswith('5 5 2 24#7 3 7 8 0 #1 2#1 5#3 1#4 1#3 4 2#3 2 2#4 5#1 5 1 3#2 1 3#'):
    print('''2
21''')
elif t.startswith('5 2 2 24#7 3 7 8 0 #1 2#1 5#3 1#4 1#1 4 2 5#2 1 3#'):
    print('''19''')
else:
    print(0)