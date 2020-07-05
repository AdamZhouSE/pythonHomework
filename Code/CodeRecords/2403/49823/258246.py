def n(a,b):
    import numpy as np
    l=np.zeros([b],dtype=int)
    for i in range(0,b):
        l[i]+=(i+1)*2+b
    print(list(l))
if __name__ == '__main__':
    n(int(input()),int(input()))
