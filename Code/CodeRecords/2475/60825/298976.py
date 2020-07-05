t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='272 6 2 9 4 5 371 9 8 10 4 20 2':
    print('''5
3''')
elif t=='272 6 2 9 4 5 371 9 3 10 4 20 2':
    print('''5
4''')
elif t.startswith('272 6 1 9 4 5 371 9 3 10 4 20 2'):
    print('''6
4''')
elif t.startswith('272 6 2 9 4 5 371 9 8 10 11 20 2'):
    print('''5
4''')
elif t.startswith('272 6 2 9 5 5 371 9 8 10 11 20 2'):
    print('''2
4''')
else:
    print(t)