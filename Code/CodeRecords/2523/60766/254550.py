# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:55:44 2020

@author: Lenovo
"""

import itertools
import collections

class Solution:
    def diagonalSort(self, mat):
        m, n, d = len(mat), len(mat[0]), collections.defaultdict(list)
        for i, j in itertools.product(range(m), range(n)):
            d[i - j].append(mat[i][j])
        d = {k: iter(sorted(v)) for k, v in d.items()}
        for i, j in itertools.product(range(m), range(n)):
            mat[i][j] = next(d[i - j])
        return mat

if __name__ == '__main__':
    num=eval(input())
    s=Solution()
    print(s.diagonalSort(num))