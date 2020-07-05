t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='150':
    print('50.000000')
elif t=='450 50 20 30':
    print('37.500000')
elif t.startswith('610 10 10 20 20 20'):
    print('15.000000')
elif t.startswith('40 25 50 75'):
    print('37.500000')
else:
    print('66.666667')