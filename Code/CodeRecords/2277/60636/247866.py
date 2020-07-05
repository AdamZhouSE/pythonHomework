def superEggDrop( K, N):
        if N==0 or N==1 or K==1:
            return N
        res = N
        for i in range(1,N):
            res = min(res,1+max(superEggDrop(K-1,i-1),superEggDrop(K,N-i)))
        return res
k=int(input())
n=int(input())
print(superEggDrop(n,k))