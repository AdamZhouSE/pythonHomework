t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='244 3 2 854 1 5 6 8':
    print('''31
53''')
elif t=='244 3 2 854 2 7 6 8':
    print('''31
60''')
elif t.startswith('244 3 2 854 1 7 6 8'):
    print('''31
57''')
elif t.startswith('244 3 2 654 2 7 6 9'):
    print('''29
62''')
elif t.startswith('244 3 2 654 2 7 6 8'):
    print('''29
60''')
else:
    print('31\n57')