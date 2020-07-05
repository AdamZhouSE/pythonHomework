from fractions import Fraction
string=input().strip("[")
string=string.strip("]")
primes=string.split(",")
primes=list(map(int,primes))
k=int(input())
def under(x):
    count=0
    best=0
    i=-1
    for j in range(1,len(primes)):
        while(primes[i+1]<primes[j]*x):
            i+=1
        count+=i+1
        if(i>=0):
            best=max(best,Fraction(primes[i],primes[j]))
    return count,best
lo,hi=0.0,1.0
while(hi-lo>1e-9):
    mi=(lo+hi)/2
    count,best=under(mi)
    if(count<k):
        lo=mi
    else:
        ans=best
        hi=mi
nu=ans.numerator
denp=ans.denominator
print("["+str(nu)+", "+str(denp)+"]")
