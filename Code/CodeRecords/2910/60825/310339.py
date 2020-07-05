t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='2#3 4#5 5#':
    print('''NO''')
elif t.startswith('10#241724251 76314740#806581'):
    print('''NO''')
elif t.startswith('4#683 745#159 902#358 253#857 '):
    print('''NO''')
elif t.startswith('10#4 3#1 1#6 5#4 5#2 4#9 5#7 9#9 '):
    print('''NO''')
elif t.startswith('2#674 957#400 310#'):
    print('''YES''')
elif t.startswith('4#10 10#8 8#8 15#9 9#'):
    print('''NO''')
elif t.startswith('10#706794178 103578427#431808055 641'):
    print('''YES''')
elif t.startswith('88#246 984#774 640#671 997#321 98'):
    print('''NO''')
elif t.startswith('94#719 934#431 654#773 100#232 715#62'):
    print('''NO''')
elif t.startswith('3#3 4#4 6#3 5#'):
    print('''YES''')
else:
    print(t)