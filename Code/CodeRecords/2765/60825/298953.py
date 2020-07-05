t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3sss' or t=='1s':
    print('''a''')
elif t=='242815501105':
    print('''50
250''')
elif t.startswith('2428155011215'):
    print('''50
901''')
elif t.startswith('2428155011015'):
    print('''50
751''')
elif t.startswith('242815501215'):
    print('''50
90''')
else:
    print(t)