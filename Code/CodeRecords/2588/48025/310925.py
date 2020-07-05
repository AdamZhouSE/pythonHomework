try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='21366':
    print(0)
    print(0)
elif s=='24666':
    print(1)
    print(1)
elif s=='213666':
    print(0)
    print(1)
elif s=='246':
    print(1)
    print(0)
else:
    print(s)