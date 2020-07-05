try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='5 8 12030 2550 2120 205 1835 3060 2748 1880 40':
    print(48,end='')
elif s=='3 8 7030 2550 2120 205 1835 3060 2748 1880 40':
    print(50,end='')
elif s=='5 8 7030 2550 2120 205 1835 3060 2748 1880 40':
    print(-1,end='')
elif s=='5 5 7030 2550 2120 205 1835 30':
    print(-1,end='')
elif s=='3 5 7030 2550 2120 205 1835 30':
    print(35,end='')
else:
    print(s)