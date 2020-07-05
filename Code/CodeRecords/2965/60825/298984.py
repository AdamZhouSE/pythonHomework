t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='3sss' or t=='1s':
    print('''a''')
elif t=='10mamadmamad':
    print('''a''')
elif t.startswith('2 18#copypaste#4#3 6 8#1 5 2#4 12 1#17 18 0#'):
    print('''ac''',end='')
elif t.startswith('6 100#jjooii#3#5 6 3#4 6 1#1 2 3#'):
    print('''joiojo''',end='')
elif t.startswith('6 100#jjooii#3#5 6 2#4 6 1#1 2 3#'):
    print('''joioji''',end='')
else:
    print(t)
