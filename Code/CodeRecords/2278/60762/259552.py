#!/usr/bin/python
# -*- coding: UTF-8 -*-
#整数转二进制三种方法--------------------------------
#你可以自己写函数采用 %2 的方式来算。
#>>> binary = lambda n: '' if n==0 else binary(n/2) + str(n%2)
#>>> binary(5)
#'101'
#>>>
#采用 python 自带了方法 bin 函数，比如 bin(12345) 回返回字符串 '0b11000000111001', 这个时候在把0b去掉即可:
#>>> bin(12345).replace('0b','')
#'11000000111001'
#也可以采用字符串的 format 方法来获取二进制：
#>>> "{0:b}".format(12345)
#'11000000111001'
#>>>
#-----------------------------------------------------
#判断全为1和0： if(l[j].count("1")+l[j].count("0")!=len(j)): l[j]=bin(int(l[j])).replace("0b","")
t=int(input())
for i in range (0,t):
    len=int(input())
    l=[int(x) for x in input().split(" ")]
    for j in range (0,len-1):
        print(l[j]^l[j+1],end=" ")
    print(l[len-1])
        






