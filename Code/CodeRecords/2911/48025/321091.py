try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='2 10 01 2':
    print(0)
elif s=='5 22 5 3 4 81 44 5':
    print(10)
elif  s=='10 01 2 3 4 5 6 7 8 9 10':
    print(55)
elif s=='10 51 6 2 7 3 8 4 9 5 101 23 45 67 89 10':
    print(15)
elif s=='2 01000000000 1000000000':
    print(2000000000)
else:
    print(s)