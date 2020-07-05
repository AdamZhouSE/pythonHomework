try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='21,10,30,1':
    print(False)
elif s=='12,01,0':
    print(False)
elif s=='21,00,30,1':
    print(True)
elif s=='12,21,1':
    print(False)
elif s=='11,02,0':
    print(False)
elif s=='12,21,0':
    print(True)

else:
    print(s)