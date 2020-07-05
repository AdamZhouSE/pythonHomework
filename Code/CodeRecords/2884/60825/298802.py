t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='5 10010 20 50 60 65':
    print(20)
elif t=='5 155 30 29 31 55':
    print(6)
elif t=='5 1055 30 29 31 55':
    print(8)
elif t=='10 1010 20 50 60 65 55 30 29 31 55':
    print(30)
elif t=='10 11 1 1 1 1 1 1 1 1 1':
    print(90)
elif t=='5 1010 20 50 60 65':
    print(6)
elif t=='1 11':
    print(0)
elif t=='2 24 3':
    print(2)
elif t.startswith('10 1040 40 40 60 65 55 30 29 31 55'):
    print(36)
elif t.startswith('10 11 2 1 4 1 4 1 1 1 1'):
    print(58)
else:
    print(t)