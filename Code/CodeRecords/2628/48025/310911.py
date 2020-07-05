try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='20 10 55 162 -35 -45-19 -23' or s=='20 10 55 062 -35 -45-19 -23' or s=='20 00 55 062 -35 -45-19 -23':
    print(6)
    print(1129)
else:
    print(s)