# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:04:26 2020

@author: Lenovo
"""

def printes(s):
    for i in range(len(s)//2):
        if s[i]==s[len(s)-1-i]:
            continue
        else:
            print(False)
            return
    print(True)

if __name__ == "__main__":
    s=input()
    printes(s)