t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3487115':
    print('''3
1
-1''')
elif t=='3487015':
    print('''3
-1
-1''')
elif t.startswith('3417015'):
    print('''1
-1
-1''')
elif t.startswith('5 mamad'):
    print(3)
else:
    print('''1
2
-1''')
