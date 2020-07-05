# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 08:16:22 2020

@author: Lenovo
"""

from math import log2
class Solution:
    #N=k^m + k^(m-1) + ... +k + 1 .  k>=2 , m>=1 ①
    def smallestGoodBase(self, n):
        n=int(n)
        m=int(log2(1+n))    #m的最大可能取值
        while m>1:
            k=int(n**(1/m)) # n≈k^m ，向下取整不会错过正解
            while True:
                d=(k**(m+1)-1) - (k-1)*n
                if d<=0:    # [k^(m+1)-1]/(k-1) <= n
                    if 0==d and k>1:    
                        return str(k)
                    break
                k-=1
            m-=1
        return str(n-1)     # k=n-1 , m=1 一定满足①

if __name__ == '__main__':
    s=Solution()
    n=int(input())
    print(s.smallestGoodBase(str(n)))