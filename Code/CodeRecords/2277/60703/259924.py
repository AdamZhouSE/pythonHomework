K = int(input())
N = int(input())
memo = dict()
import sys

def dp(K,N):
    if(K==1):
        return N
    if(N==0):
        return 0
    if((K,N) in memo):
        return memo[(K,N)]
    res = sys.maxsize
    for i in range(1,N+1):
        res = min(
            res,max(dp(K,N-i),dp(K-1,i-1))+1
        )
    memo[(K,N)] = res#计入备忘录
    return res

print(dp(K,N))
