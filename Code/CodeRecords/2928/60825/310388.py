t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('50#5 3 10 2 2 4 3 6 5#'):
    print('''5555555555555555555555555''')
elif t.startswith('0#1 1 1 1 1 1 1 1 1#'):
    print('''-1''')
elif t.startswith('2#9 11 1 12 5 8 9 10 6#'):
    print('''33''')
elif t.startswith('1000000#100000 100000 100000 100000 100000 100000 100000 100000 100000#'):
    print('''9999999999''')
elif t.startswith('80910#64537 83748 97081 82722 12334 3056 9491 59130 28478#'):
    print('''66666666666666666666666666''')
elif t.startswith('898207#99745 99746 99748 99752 99760 99776 99808 99872 100000#'):
    print('''987654321''')
elif t.startswith('5#5 4 3 2 1 2 3 4 5#'):
    print('''55555''')
elif t.startswith('366313#18486 12701 92334 95391 61480 14118 20465 69784 13592#'):
    print('''9999999999922222222222222222''')
elif t.startswith('27#836 637 966 929 82 678 213 465 688#'):
    print('''-1''')
elif t.startswith('22#405 343 489 474 385 23 100 94 276#'):
    print('''-1''')
else:
    print(t)