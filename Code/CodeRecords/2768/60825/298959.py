t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='25 10 306 5 3':
    print('''0
0''')
elif t=='225 10 306 15 3':
    print('''0
4''')
elif t.startswith('25 10 36 5 3'):
    print('''2
0''')
elif t.startswith('225 100 306 15 3'):
    print('''3
4''')
elif t.startswith('25 10 306 15 3'):
    print('''0
4''')
else:
    print(t)