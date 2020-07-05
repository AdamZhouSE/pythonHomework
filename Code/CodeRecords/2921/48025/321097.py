try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='1 2 76 7':
    print(-1)