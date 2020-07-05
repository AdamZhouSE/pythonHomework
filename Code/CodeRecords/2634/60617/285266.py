from fractions import Fraction

def frac_bs():
    arr = eval(input())
    K = int(input())
    count=0
    best=0
    def under(x):
        count, best = 0,0
        i = -1
        for j in range(1, len(arr)):
            while arr[i+1]<arr[j]*x:
                i+=1
            count+=i+1
            if i>=0:
                best=max(best,Fraction(arr[i],arr[j]))
        return count, best
    l,r=0.0,1.0
    while r-l>10**-9:
        mid=(l+r)/2.0
        count,best=under(mid)
        if count>=K:
            res=best
            r=mid
        else:
            l=mid
    print([res.numerator,res.denominator])

if __name__=='__main__':
    frac_bs()