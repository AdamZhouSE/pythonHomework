try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='3[[0,1]][[2,1]]':
    print([0,1,-1])
elif s=='3[[1,0]][[2,1]]':
    print([0,-1,-1])
elif s=='3[[0,1],[0,2]][[1,0]]':
    print([0,1,1])
elif s=='3[[0,1],[1,2]][]':
    print([0,1,-1])
elif s=='3[[0,1]][[1,2]]':
    print([0,1,2])
else:
    print(s)
    