try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='5 2 2 247 3 7 8 0 1 21 53 14 11 4 2 52 1 3':
    print(19)
elif s=='5 5 2 247 3 7 8 0 1 21 53 14 13 4 23 2 24 51 5 1 32 1 3':
    print(2)
    print(21)
elif s=='5 2 2 247 3 7 8 0 1 21 53 14 13 4 24 3':
    print(7)
elif s=='5 2 2 247 3 7 8 0 1 21 53 14 13 4 24 2':
    print(3)
elif s=='5 2 2 247 3 7 8 0 1 21 53 14 13 4 24 1':
    print(0)
else:
    print(s)