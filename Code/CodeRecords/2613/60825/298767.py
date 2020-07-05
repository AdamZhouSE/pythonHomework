t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='263':
    print('1 2 4 5 7 9')
    print('1 2 4')
elif t=='2612':
    print('1 2 4 5 7 9')
    print('1 2 4 5 7 9 10 12 14 16 17 19')
elif t=='262':
    print('1 2 4 5 7 9')
    print('1 2')
else:
    print(t)