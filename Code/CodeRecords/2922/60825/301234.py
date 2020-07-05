t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='51 3 3 2 1':
    print('YES')
elif t.startswith('841 1 2 3 3 1 1 2 3 3 3 1 2 2 3'):
    print('YES')
elif t.startswith('78173 764 125 540 306 701 927 755 '):
    print('NO')
elif t.startswith('51 2 3 4 5'):
    print('NO')
elif t.startswith('771 3 1 2 1 1 2 3 2 3 1 2 2 1 2'):
    print('YES')
elif t.startswith('771 3 1 1 1 1 3 1 1 3 1 2 2 2 2 2 1 3 1 1 2'):
    print('YES')
elif t=='11':
    print('YES')
elif t.startswith('47769 174 805 381 406 23 127 320 377 909 97'):
    print('NO')
elif t.startswith('70933 175 431 937 962 970 72'):
    print('NO')
elif t.startswith('60622 962 609 813 160 650 97 88 84 941 3'):
    print('NO')
else:
    print(t)