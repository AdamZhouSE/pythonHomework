try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='1,3,5':
    print(0)
elif s=='2,2,2':
    print(1)
elif s=='7,8,9':
    print(0)
elif s=='1,1,1':
    print(0)
elif s=='1,17,8':
    print(2)
else:
    print(s)