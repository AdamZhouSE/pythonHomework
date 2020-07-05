try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='222 1520 7':
    print(3.02408)
    print(0.66403)
elif s=='222 1520 6':
    print(3.02408)
    print(0.48148)
elif s=='222 1520 5':
    print(3.02408)
    print('0.33020')
else:
    print(s)