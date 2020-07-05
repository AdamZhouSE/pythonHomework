#!/usr/bin/python
# -*- coding: UTF-8 -*-s=input()
#1.首先带奇环的显然是 NO;
#2.否则对于每个连通块，递归删掉所有度数为1的点（即将支出去的外向树删掉）:
#剩下的是偶环，显然是 YES；
#剩下的图只有两个度数为3的点，那么这两个点之间有3条路径，这三条路径上边数次为2,2,even(偶数)则是 YES；
#其他情况全为 NO。
t=int(input())
for g in range (0,t):
    s=input().split(" ")
    n=int(s[0])
    m=int(s[1])
    l=[[] for i in range (n+1)]
    for i in range (0,m):
        ss=[int(x) for x in input().split(" ")]
        l[ss[0]].append(ss[1])
        l[ss[1]].append(ss[0])
    print(l)
    re=0
    










