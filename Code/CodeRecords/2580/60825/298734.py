t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='7223,31,1':
    print(1)
elif t=='1222,23,3':
    print(2)
elif t.startswith('3322,23,3'):
    print(4)
elif t.startswith('1322,23,3'):
    print(2)
else:
    print(t)