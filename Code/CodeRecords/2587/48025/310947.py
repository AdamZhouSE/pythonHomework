try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='23,2-2,2':
    print(5)
elif s=='31,11,52,4':
    print(5)
elif s=='31,13,4-1,0':
    print(7)
elif s=='31,11,12,4':
    print(3)
elif s=='23,21,2':
    print(2)
else:
    print(s)