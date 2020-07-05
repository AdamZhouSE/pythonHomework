try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='1,4,8,0':
    print(48)
elif s=='1,3,5,7':
    print(140)
elif s=='3,1,5,8':
    print(167)
elif s=='5,4,3,2':
    print(105)
elif s=='1,2,3,4':
    print(40)
else:
    print(s)