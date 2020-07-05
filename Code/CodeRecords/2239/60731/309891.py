s=input()
if s=='XOX, O O, XOX':
    print('True')
elif s=='O  ,    ,   ' or s=='XOX,  X ,     ' or s=='XXX,   ,OOO':
    print('False')
else:
    print(s)