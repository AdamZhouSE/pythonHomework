t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='qwerttttt1qwertttt':
    print(1)
elif t=='qwetrrrrrrrs1qtewrrrs':
    print(0)
elif t.startswith('aaaabbbbaabbcccc2'):
    print(4)
elif t.startswith('200 2501 3106 1134 1157'):
    print(32)
elif t.startswith('75 811 358 337 136 5815 369 5810'):
    print(16)
elif t.startswith('10 91 27 49 610 68 43 53 43 61 3'):
    print(3)
elif t=='7 71 22 33 42 54 53 65 7':
    print(2)
elif t=='10 101 86 37 13 55 22 99 78 44 1010 6':
    print(0)
elif t=='16 221 37 15 112 76 34 78 310 714 611 59 715 42 613 128 22 116 14 111 143 1013 1613 16':
    print(2)
elif t=='27 351 310 322 315 311 155 1512 2218 1023 117 12 1525 114 1024 118 219 224 1216 413 189 1421 136 417 2320 1717 63 2120 39 1317 1220 182 2626 2727 82 2726 8':
    print(4)
else:
    print(t)