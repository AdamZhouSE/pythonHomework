def superEggDrop( K, N):
        if N==0 or N==1 or K==1:
            return N
        res = N
        for i in range(1,N):
            if (K-1,i-1) in d:
                c1 = d[(K-1,i-1)]
            else:
                c1=self.superEggDrop(K-1,i-1)
                d[(K-1,i-1)]=c1
            if (K,N-i) in d:
                c2 = d[(K,N-i)]
            else:
                c2=self.superEggDrop(K,N-i)
                d[(K,N-i)]=c2
            res = min(res,1+max(c1,c2))
        return res

k=int(input())
n=int(input())
print(superEggDrop(n,k))