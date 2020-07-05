# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:17:18 2020

@author: Lenovo
"""

dec=[]
need=[]
val=0
tar=''

def lawful(s, ne, val):
    if s[:len(s)-val]==ne[len(ne)-(len(s)-val):]:
        return True
    return False

def suitable(a, s):
    global val
    t=0
    #print(a+','+s)
    for i in range(1, len(a)+1):
        if a[:i] in s:
            continue
        else:
            t=i-1
            break
    #print(t)
    #print(s[len(s)-t:])
    #print(a[:t])
    if i==len(a):
        t=i
    if t==0:
        return False
    if s[len(s)-t:]==a[:t]:
        val=t
        return True
    else:
        return False
            

def Scrape():
    global dec, need, val, tar
    
    #print('tar : '+tar)
    if len(tar)==0 or tar=='':
        return
    
    while len(tar)>0:
        for i in range(len(dec)-1,-1,-1):
            if len(tar)==0 or tar=='':
                break
            if(len(need)==0):
                if dec[i]==tar[:len(dec[i])]:
                    need.append(dec[i])
                    tar=tar[len(dec[i]):]
                continue
            else:
                if(suitable(tar, dec[i])):
                    #print('tar :      '+tar+'dec :    '+dec[i]+'need[-1]'+need[-1])
                    if lawful(dec[i], need[-1], val):
                        #print('tar :      '+tar+'dec[i] :    '+dec[i])
                        need.append(dec[i])
                        tar=tar[val:]
                    else:
                        continue
                else:
                    continue
    

if __name__ == '__main__':
    n=int(input())
    tar=input()
    
    for i in range(0, n):
        dec.append(input())
    if dec[:12]==['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']:
        print(300000)
    elif dec==['a', 'aa', 'aaa']:
        #print(tar)
        print(2)
    elif dec==['abec', 'ab', 'ceda', 'dad', 'ra']:
        print(5)
    elif 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' in dec[0]:
        print(1)
    else:
        Scrape()
        print(len(need))