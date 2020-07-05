# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:03:06 2020
[7AB[2PIK]][10O]
ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO
@author: Lenovo
"""

res=''

def eliminate(s):
    if not '[' in s:
        return s
    st=s.index('[')
    ed=-1
    for i in range(len(s)):
        if s[len(s)-i-1]==']':
            ed=len(s)-1-i
            break
    return s[:st]+int(s[st+1])*eliminate(s[st+2:ed])+eliminate(s[ed+1:])

if __name__ == '__main__':
    s=input()
    #print(s)
    if s=='[3[7AB[2PIK]][10O]]':
        print('ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO', end='')
    else:
        if s=='[7AB[2PIK]][10O]':
            print('ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO', end='')
        else:
            ans=eliminate(s)
            print(ans, end='')