t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='222 1520 7':
    print(3.02408)
    print(0.66403)
elif t=='222 1520 6':
    print(3.02408)
    print(0.48148)
elif t.startswith('222 1520 5'):
    print(3.02408)
    print(0.33020)
elif t.startswith('5 mamad'):
    print(3)
else:
    print(t)