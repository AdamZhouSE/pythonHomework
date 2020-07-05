# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:09:07 2020
s = "kiss", t = "kill"
@author: Lenovo
"""

def lawful(s, t):
    return len(s) == len(t) and all([s.count(i) == t.count(i) for i in set(s)])  
    
if __name__ == "__main__":
    line=input().split(',')
    s=line[0][5:-1]
    p=line[1][6:-1]
    #print(s)
    #print(p)
    
    
    if lawful(s, p):
        print('true')
    else:
        print('false')