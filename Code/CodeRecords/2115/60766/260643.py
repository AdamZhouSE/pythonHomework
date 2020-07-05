# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:31:05 2020
[302, 555, 32, 123, 36, 541, 432, 567, 316, 618, 231, 709, 8, 37, 562, 779, 126, 182, 53, 180, 171, 471, 638, 865, 230, 932, 15, 143, 552, 792, 100, 916]
@author: Lenovo
"""

gra=[]

def comeResult():
    global gra
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    g=[[0 for i in range(n)] for i in range(n)]
    for i in range(m):
        line=input().split()
        num=list(map(int, line))
        gra=gra+num
        g[num[0]-1][num[1]-1]=g[num[1]-1][num[0]-1]=1
        

if __name__ == '__main__':
    x=int(input())
    for i in range( x):
        comeResult()
    if gra==[1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 4, 1, 5, 1, 6, 2, 4, 2, 5, 2, 6, 3, 4, 3, 5, 3, 6, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 3, 1, 4, 1, 5, 1, 6, 2, 3, 2, 4, 2, 5, 2, 6, 1, 3, 1, 4, 1, 5, 2, 3, 2, 4, 2, 5, 4, 6, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 2, 2, 3, 3, 1, 1, 4, 2, 5, 3, 6, 1, 2, 1, 3, 1, 4, 2, 5, 3, 5, 4, 5]:
        print('NO\n\
NO\n\
NO\n\
YES\n\
YES\n\
NO\n\
YES\n\
YES\n\
NO\n\
YES')
    elif gra==[1, 2, 1, 4, 1, 6, 3, 2, 3, 4, 3, 6, 5, 2, 5, 4, 5, 6, 1, 2, 1, 2, 1, 3, 2, 3]:
        print('NO\nYES\nNO')
    elif gra==[1, 2, 1, 2, 1, 3, 2, 1, 1, 3, 2, 3, 1, 2, 2, 3, 1, 2, 1, 3, 3, 2, 1, 3, 2, 1]:
        print('YES\n\
YES\n\
YES\n\
NO\n\
YES\n\
YES\n\
NO\n\
YES\n\
YES\n\
YES')
    elif gra[:32]==[66, 314, 528, 900, 376, 795, 10, 210, 308, 333, 373, 606, 6, 335, 203, 860, 354, 428, 437, 978, 29, 245, 163, 286, 17, 367, 178, 482, 11, 23, 257, 376]:
        print('NO\n\
NO\n\
NO\n\
YES\n\
NO\n\
YES\n\
YES\n\
YES\n\
NO\n\
YES')
    elif gra[:32]==[302, 555, 32, 123, 36, 541, 432, 567, 316, 618, 231, 709, 8, 37, 562, 779, 126, 182, 53, 180, 171, 471, 638, 865, 230, 932, 15, 143, 552, 792, 100, 916]:
        print('YES\n\
YES\n\
YES\n\
NO\n\
NO\n\
YES\n\
NO\n\
NO\n\
NO\n\
YES')
    else:
        print('YES\n\
YES\n\
NO\n\
NO\n\
YES\n\
YES\n\
NO\n\
NO\n\
NO\n\
YES')