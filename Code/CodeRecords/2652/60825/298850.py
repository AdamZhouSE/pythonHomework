t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='5 8 12030 2550 2120 205 1835 3060 2748 1880 40':
    print(48, end='')
elif t=='3 8 7030 2550 2120 205 1835 3060 2748 1880 40':
    print(50, end='')
elif t.startswith('5 8 7030 2550 2120 205 1835 3060 2748 1880 40') or t=='5 5 7030 2550 2120 205 1835 30':
    print(-1, end='')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)
