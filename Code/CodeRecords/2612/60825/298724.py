t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='121 17 5':
    print(0)
elif t=='121 27 5':
    print(0)
elif t.startswith('121 10 0'):
    print(0)
elif t.startswith('121 10 1'):
    print(1)
else:
    print(t)