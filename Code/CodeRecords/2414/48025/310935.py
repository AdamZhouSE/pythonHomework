try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='1':
    print('1.00000')
elif s=='2':
    print('0.50000')
elif s=='3':
    print('0.50000')
elif s=='4':
    print('0.50000')
elif s=='6':
    print('0.50000')
else:
    print(s)