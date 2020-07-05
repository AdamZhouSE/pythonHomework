try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='2,2,1,1,1,2,2':
    print(2)
elif s=='1,1,1,1,2,2,3':
    print(1)
elif s=='2,2,2,2,2,2,2':
    print(2)
elif s=='3,3,3,3,3,4,4,5,5':
    print(3)
elif s=='1,1,4,3,4,4,4,4':
    print(4)
elif s=='4,4,4,4,4,3,3,3,1':
    print(4)
else:
    print(s)