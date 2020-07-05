# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:42:49 2020

@author: Lenovo
"""

from functools import cmp_to_key

def largestNumber(nums):
    key = cmp_to_key(lambda a,b: int(b+a)-int(a+b))
    res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
    return res or '0'

if __name__ == '__main__':
    nums=eval(input())
    n=largestNumber(nums)
    print(n)