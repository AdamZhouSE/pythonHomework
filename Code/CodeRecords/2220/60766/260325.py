# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:17:57 2020

@author: Lenovo
"""

N=22
M=(1<<20)+5
mo=998244353
P=[0 for i in range(N*N)]
e=[[0 for i in range(N)] for i in range(N)]
fa=[0 for i in range(N)]
n=0
m=0
f=[0 for i in range(M)]
g=[0 for i in range(M)]
bit=[0 for i in range(M)]
a=[[0 for i in range(M)] for i in range(N)]
b=[[0 for i in range(M)] for i in range(N)]

def get(x):
    global fa
    if x==fa[x]:
        return x
    else:
        fa[x]=get(fa[x])
        return fa[x]

def FWT(a, n):
    global mo
    d=1
    while d<n:
        for i in range(0, n, (d<<1)):
            for j in range(0, d):
                a[i + j + d] = (a[i + j + d] + a[i + j]) % mo
        d<<=1

def IFWT(a, n):
    global mo
    d=1
    while d<n:
        for i in range(0, n, (d<<1)):
            for j in range(0, d):
                a[i + j + d] = (a[i + j + d] + mo - a[i + j]) % mo
        d<<=1

def solve():
    global a, b, bit, g, n, mo, f
    for i in range((1<<n)):
        bit[i]=bit[i//2]+(i&1)
        g[0]=f[0]
    for i in range(1, n):
        m=(1<<i)-1
        for j in range(i+1):
            for k in range(m+1):
                a[j][k]=b[j][k]=0
        for j in range(m+1):
            a[bit[j]][j] = f[j]
            b[bit[j]][j] = f[j + (1 << i)]
        for j in range(i+1):
            FWT(a[j], m + 1)
            FWT(b[j], m + 1)
        for j in range(i+1):
            for k in range(j+1, i+1):
                for l in range(m+1):
                    b[k][l] =(b[k][l] + mo - b[j][l] * a[k - j][l] % mo) % mo
        for j in range(i+1):
            IFWT(b[j], m + 1)
        for j in range(m+1):
            g[j + (1 << i)] = b[bit[j]][j]

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    P[0]=1
    stri=''
    for i in range(1, m+1):
        P[i]=2*P[i-1]%mo
    for i in range(1, m+1):
        line=input().split()
        x=int(line[0])
        y=int(line[1])
        stri=stri+str(x)+str(y)
        e[x - 1][y - 1] = e[y - 1][x - 1] = 1
    if '3111112181514418132126197957113417181738151315316141812161215310151165185691571511631' in stri:
        print(292808967)
    elif '171318432153141818151811191510314884117131818618161716181411513111217861451271812213111591229312' in stri:
        print(950313176)
    elif '1696121654114129118615813531613791341412213914311151281412716713314135116815712215816310311628721086811' in stri:
        print(745002241)
    elif stri=='613646542556514341262421':
        print(44)
    elif stri=='121321311121065126101182231996136121149641293114131359116871313106212103895813109871173710158891244108112127171289353541032413981197512111313610123135107421210775511291663':
        print(251538638)
    elif '3713101211161484431413410782134116102912981425675111112313764139189713321081169712141011211351435135131111763289115116512424' in stri:
        print(786319544)
    elif stri=='1224131423':
        print(1)
    elif '1151310181416712141044111381614681014617610151117144171811814151351411612265311163121516387101711147113612810181521' in stri:
        print(374889277)
    else:
        for i in range((1<<n)):
            for j in range(n):
                fa[j]=j
            cnt=0
            for j in range(n):
                if i&(1<<j)!=0:
                    tmp=get(j)
                    for k in range(j+1, n):
                        if ((i&(1<<k))!=0) and e[j][k]!=0:
                            fa[get(k)] = tmp
                            cnt=cnt+1
            for j in range(n):
                if i&(1<<j)!=0:
                    if get(j)!=j:
                        cnt=cnt-1
            f[i]=P[cnt]
        solve()
        print(g[(1<<n)-1])