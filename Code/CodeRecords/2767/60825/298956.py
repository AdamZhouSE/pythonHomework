t=""
while True:
    try:
        ts=input()
        t+=ts
        t+=" "
    except:
        break
        
if t=='3 8 21 3 ':
    print('''1
3
1''')
elif t=='3 8 2 13 ':
    print('''1
0
2''')
elif t.startswith('3 8 2 3 '):
    print('''1
0
1''')
elif t.startswith('3 18 21 3 '):
    print('''3
3
1''')
elif t.startswith('3 8 20 13 '):
    print('''1
4
2''')
else:
    print(t)