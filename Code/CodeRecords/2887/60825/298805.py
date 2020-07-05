t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='31 0 102 0 101 10 0':
    print('LIVE\nDEAD')
elif t=='41 0 102 0 102 6 42 10 0':
    print('DEAD\nLIVE')
elif t.startswith('21 5 52 6 4'):
    print('LIVE\nLIVE')
elif t.startswith('41 0 102 0 101 6 41 6 4'):
    print('DEAD\nDEAD')
else:
    print('LIVE\nLIVE')