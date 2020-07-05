def n(a,b):
    import numpy as np
    l=np.zeros([b],dtype=int)
    i=0
    t=0
    while a>0:
        l[i]+=min(t*b+i+1,a)
        a-=t*b+i+1
        t+=int((i+1)==b)
        i=(i+1)%b
    print(list(l))
if __name__ == '__main__':
    n(int(input()),int(input()))
