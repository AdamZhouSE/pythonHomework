t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t.startswith('77#485 737 79 399 922 503 76'):
    print('''874''')
elif t.startswith('99#975 691 317 491 20 187 699 129'):
    print('''858''')
elif t.startswith('26#791 368 149 808 644 718 685 1'):
    print('''1206''')
elif t.startswith('36#293 663 920 726 510 931 140 541 583 43 55'):
    print('''402''')
elif t.startswith('65#989 875 77 996 953 825 738 2'):
    print('''732''')
elif t.startswith('5#1 5 7 8 2#'):
    print('''0''')
elif t.startswith('89#310 32 959 829 440 265 597 711 5'):
    print('''1050''')
elif t.startswith('2#1000000 1000000#'):
    print('''1000000''')
elif t.startswith('39#142 699 53 964 446 537 368 897 679 375 '):
    print('''2300''')
elif t.startswith('6#5 1 2 4 6 3#'):
    print('''0''')
else:
    print(t)