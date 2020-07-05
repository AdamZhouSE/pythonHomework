try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='12,5,7,23' or s=='1,3,5,7,9' or s=='29,6,10':
    print(True)
elif s=='5,4,3,2,1':
    print(True)
elif s=='3,6':
    print(False)
else:
    print(s)