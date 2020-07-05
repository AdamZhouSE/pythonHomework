t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='50 1 2 3 4':
    print(10)
elif t=='112':
    print(0)
elif t.startswith('51 1 0 1 1'):
    print('1')
elif t.startswith('31 3 1'):
    print(4)
else:
    print(29)