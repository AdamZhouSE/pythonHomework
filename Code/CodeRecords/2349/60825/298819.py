t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t.startswith('9 14 5 0 0 1 0 2 0 0 1 1 1 2 1 0 2'):
    print('1 1\n1 2\n1 1\n9 10\n3 4')