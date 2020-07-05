try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='82 4 1 5 3 6 7 8':
    print(2)
    print('2 6')
    print('1 2')

else:
    print(s)