while True:
    try:
        n=int(input().strip())
        inp=list(map(int,input().strip().split(' ')))
        d=int(input().strip())
        tree=[]
        left=0
        for i in range(d-1):
            left+=2**i
        right=left+2**(d-1)
        tree=inp[left:right]
        if len(tree)==0:
            print('EMPTY')
        else:
            print(' '.join(map(str,tree)))
             
    except:
        break