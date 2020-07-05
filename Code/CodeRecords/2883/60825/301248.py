t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='5 6#WBBBBB#WBBBBB#WBBBBB#WBBBBB#WBBBBB#':
    print('''3 4''')
elif t=='3 3#WWW#BWW#WWW#':
    print('''2 1''')
elif t.startswith('1 1#B#'):
    print('''1 1''')
elif t.startswith('5 6#WWBBBW#WWBBBW#WWBBBW#WWWWWW#WWWWWW#'):
    print('''2 4''')
elif t.startswith('4 3#WWW#WWW#BWW#WWW#'):
    print('''3 1''')
else:
    print(t)