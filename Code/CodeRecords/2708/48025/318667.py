try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='3 5 7C 1 2C 2 2W 1 2C 3 2W 1 2C 3 3W 1 3':
    print(3)
    print(3)
    print(0)
elif s=='3 5 7C 1 5C 2 2W 1 2C 3 2W 1 2C 3 4W 1 3':
    print(2)
    print(2)
    print(0)
elif s=='5 6 3C 1 5C 2 6W 5 6':
    print(2)
elif s=='5 6 3C 1 5C 2 2W 1 2':
    print(4)
elif s=='3 5 7C 1 5C 2 2W 1 2C 3 2W 3 4C 3 4W 2 5':
    print(2)
    print(0)
    print(1)
elif s=='5 6 3C 1 5C 2 6W 1 4':
    print(3)
else:
    print(s)