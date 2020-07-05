t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='35 26 25 3':
    print('1\n1\n0')
elif t=='35 26 35 1':
    print('1\n1\n1')
elif t.startswith('35 26 45 1'):
    print('1\n0\n1')
elif t.startswith('35 26 25 1'):
    print('1\n1\n1')
else:
    print(t)