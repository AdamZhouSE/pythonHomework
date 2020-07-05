def bj(label):
    from math import log2
    from collections import deque
    lev=int(log2(label))+1
    ans=deque([])
    n=label
    inv=2**lev
    while n>0:
        ans.appendleft(n)
        n=(inv-n-1+inv//2)//2
        inv//=2
    print(str(ans)[6:-1])
if __name__ == '__main__':
    bj(int(input()))
