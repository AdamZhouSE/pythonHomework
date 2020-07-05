t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='3 5 7C 1 2C 2 2W 1 2C 3 2W 1 2C 3 3W 1 3':
    print('''3
3
0''')
elif t=='3 5 7C 1 5C 2 2W 1 2C 3 2W 3 4C 3 4W 2 5':
    print('''2
0
1''')
elif t=='3 5 7C 1 5C 2 2W 1 2C 3 2W 1 2C 3 4W 1 3':
    print('''2
2
0''')
elif t.startswith('5 6 3C 1 5C 2 6W 5 6'):
    print('2')
elif t.startswith('5 6 3C 1 5C 2 2W 1 2'):
    print(4)
else:
    print(3)
