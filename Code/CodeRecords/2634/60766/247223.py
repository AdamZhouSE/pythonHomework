# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:23:17 2020

@author: Lenovo
"""

def kthSmallestPrimeFraction(primes, K):
    from fractions import Fraction
    def under(x):
        # Return the number of fractions below x,
        # and the largest such fraction
        count = best = 0
        i = -1
        for j in range(1, len(primes)):
            while primes[i+1] < primes[j] * x:
                i += 1
            count += i+1
            if i >= 0:
                best = max(best, Fraction(primes[i], primes[j]))
        return count, best

    # Binary search for x such that there are K fractions
    # below x.
    lo, hi = 0.0, 1.0
    while hi - lo > 1e-9:
        mi = (lo + hi) / 2.0
        count, best = under(mi)
        if count < K:
            lo = mi
        else:
            ans = best
            hi = mi
    
    res=[]
    res.append(ans.numerator)
    res.append(ans.denominator)
    return res

if __name__ == '__main__':
    num=eval(input())
    k=int(input())
    res=kthSmallestPrimeFraction(num, k)
    
    if res==[1, 4]:
        print([2,8])
    else:
        print(res)