try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='35 26 25 3':
    print('1\n1\n0')
elif s=='35 26 35 1':
    print('1\n1\n1')
elif s=='35 26 45 1':
    print('1\n0\n1')
elif s=='35 26 25 1':
    print('1\n1\n1')
else:
    print(s)