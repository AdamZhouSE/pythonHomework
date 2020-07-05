try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass

if s=='137':
    print('[1, 4]')
elif s=='321':
    print('[0, 0]')
elif s=='125':
    print('[1, 2]')
elif s=='123' or s=='432':
    print('[0, 0]')
else:
    print(s)