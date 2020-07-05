def test():
    t = int(input())
    for _ in range(0, t):
        lgp=input().split()
        l=int(lgp[0])
        g=int(lgp[1])
        p=int(lgp[2])
        l_score=0
        g_score=0
        while p!=1:
            if l%p==0:
                l_score=l_score+1
                l=l-1
            elif g%p==0:
                g_score=g_score+1
                g=g-1
            else:
                p=p-1
        print(str(l_score)+' '+str(g_score))
        

test()