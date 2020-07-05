# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:23:23 2020

@author: Lenovo
"""

def judgeSquareSum(c):
        """
        :type c: int
        :rtype: bool
        """
        n=int(c**0.5)
        left=0
        right=n
        while left<=right:
            tmp=left**2+right**2
            if c==tmp:
                return True
            if tmp<c:
                left+=1
            if tmp>c:
                right-=1
        return False
    
if __name__ == '__main__':
    n=int(input())
    print(judgeSquareSum(n))