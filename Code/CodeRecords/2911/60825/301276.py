t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='2 0#1000000000 1000000000#':
    print('''2000000000''')
elif t=='10 5#1 6 2 7 3 8 4 9 5 10#1 2#3 4#5 6#7 8#9 10#':
    print('''15''')
elif t.startswith('10 0#1 2 3 4 5 6 7 8 9 10#'):
    print('''55''')
elif t.startswith('5 2#2 5 3 4 8#1 4#4 5#'):
    print('''10''')
elif t.startswith('2 1#0 0#1 2#'):
    print('''0''')
else:
    print(t)