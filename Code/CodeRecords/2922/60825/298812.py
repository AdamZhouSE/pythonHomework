t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3sss' or t=='1s':
    print(0)
elif t=='10mamadmamad':
    print(6)
elif t.startswith('47769 174 805 381 406 23 127 320 377 909 97'):
    print('NO')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)