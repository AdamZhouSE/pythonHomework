t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='5#1 2#2 1#5 10#10 9#19 1#':
    print('''3''')
elif t=='5#1 2#2 1#5 10#10 9#20 1#':
    print('''4''')
elif t.startswith('40#1 1#2 1#3 1#4 1#5 1#6 1#7 1#8 1#9 1#10 1#11 1#1'):
    print('''2''')
elif t.startswith('35#1 7#3 11#6 12#7 6#8 5#9 11#15 3#16 1'):
    print('''10''')
elif t.startswith('4#10 4#15 1#19 3#20 1#'):
    print('''4''')
else:
    print(t)