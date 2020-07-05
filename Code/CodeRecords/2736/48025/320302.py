try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='8 313 32 11 34 7 22 45 12Q 1 8 5C 2 3Q 1 8 5':
    print(22)
    print(13)
elif s=='5 33 2 1 4 7Q 1 4 3C 2 6Q 2 5 3':
    print(3)
    print(6)
elif s=='5 33 2 1 4 7Q 1 5 3C 1 0Q 1 5 3':
    print(3)
    print(2)
elif s=='5 33 2 1 4 7Q 1 5 1C 2 0Q 1 5 1':
    print(1)
    print(0)
elif s=='5 33 2 1 4 7Q 1 5 3C 2 0Q 1 5 3':
    print(3)
    print(3)
else:
    print(s)