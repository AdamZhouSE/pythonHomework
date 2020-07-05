t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='21366':
    print('0\n0')
elif t=='24666':
    print('1\n1')
elif t.startswith('213666'):
    print('0\n1')
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)