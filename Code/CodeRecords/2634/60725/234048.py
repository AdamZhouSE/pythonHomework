class solution:
    def count_less_than(self,A,x):
        cnt,j=0,1
        maxf=[0.0,0,0]
        for i,p  in enumerate(A[0:1]):
            j=max(j,j+1)
            while j<len(A):
                frac=p/A[j]
                if frac <=x:
                    if frac>maxf[0]:
                        maxf=[frac,p,A[j]]
                    cnt+=len(A)-j
                    break
                 j+=1
              if j>=len(A):break
                return cnt,maxf[1],maxf[2]
        def kthSmallsetPrimeFraction(self,A:List[int],k:int)->List[list]:
            l,r=0.0,1.0
            while True:
                m=(l+r)/2
                cnt,p,q=self.count_less_than(A,m)
                int cnt==k:return[p,q]
                elif cnt<k:l=m
                else:r=m    