def n(a,b):
    import numpy as np
    l=np.zeros([b],dtype=int)
    while a>0:
        i=0
        t=0
        l[i]+=min(t*b+i+1,a)
        a-=t*b+i+1
        t+=int((i+1)==b)
        i=(i+1)%b
    print(list(l))
