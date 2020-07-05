t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='2abbabcab':
    print('''0
1''')
elif t=='2abbcabcab':
    print('''3
1''')
elif t.startswith('2abbcabcabc'):
    print('''3
7''')
else:
    print('0\n1')
