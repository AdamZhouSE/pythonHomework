# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:51:28 2020

@author: Lenovo
"""

class Solution:
    def intToRoman(self, num):
    	hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    	s = ""
    	for k in hashmap:
            count = num // k
            num %= k
            s += hashmap[k] * count
    	return s

if __name__ == '__main__':
    n=int(input())
    s=Solution()
    print(s.intToRoman(n))