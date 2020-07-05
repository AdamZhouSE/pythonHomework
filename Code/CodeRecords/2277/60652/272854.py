K=int(input())
N=int(input())
def minMoves(K,N):
    if K==0:
        return 0
    if K==1:
        return N
    if N==1 or N==2:
        return N
    if N%2==0:
        return 1+minMoves(K-1,N//2-1)
    else:
        return 1+minMoves(K-1,N//2)
print(minMoves(K,N)) 
