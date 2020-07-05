num_array=input()
K=int(input())
def count_less_than(A,x):
    cnt,j=0,1
    maxf=[0.0,0,0]
    for i,p in enumerate(A[0:-1]):
        j=max(j,i+1)
        while j<len(A):
            frac=p/A[j]
            if frac<=x:
                if frac> maxf[0]:
                    maxf[0]=[frac,p,A[j]]
                cnt+=len(A)-j
                break
            j+=1
        if j>=len(A):
            break
    return cnt,maxf[1],maxf[2]
def kthSmallestPrimeFraction(A,K):
    l=0.0
    r=1.0
    while True:
        m=(l+r)/2
        cnt,p,q=count_less_than(A,m)
        if cnt==K: return[p,q]
        elif cnt<K:
            l=m
        else:
            r=m
print(kthSmallestPrimeFraction(num_array,K))