# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:16:26 2020

@author: Lenovo
"""

class Solution:
    def romanToInt(self, s):
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

if __name__ == '__main__':
    s=Solution()
    stri=input()
    print(s.romanToInt(stri))