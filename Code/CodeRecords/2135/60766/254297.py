# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:54:50 2020

@author: Lenovo
"""

def minMoves2(a):
        a.sort()
        i, j = 0, len(a)-1
        ans = 0
        while i<j:
            ans += a[j]-a[i]
            i += 1
            j -= 1     
        return ans

if __name__ == '__main__':
    line=input().split(',')
    print(minMoves2(list(map(int, line))))