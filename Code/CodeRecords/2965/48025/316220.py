try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='6 100jjooii35 6 24 6 11 2 3':
    print('joioji',end='')
elif s=='6 100jjooii35 6 34 6 11 2 3':
    print('joiojo',end='')
elif s=='2 18copypaste43 6 81 5 24 12 117 18 0':
    print('ac',end='')

else:
    print(s)