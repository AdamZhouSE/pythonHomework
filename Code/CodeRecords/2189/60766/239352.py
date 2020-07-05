# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:27:44 2020

@author: Lenovo
"""

def isHappy(n):
    numList = [n]    #存放所有计算出来的数，用于判断是否存在环
    while n!=1:     #如该计算结果为1，说明该数是快乐的数
        sum=0
        for i in str(n):
            sum += int(i)**2
        if sum not in numList:     #判断是否存在环
            numList.append(sum)
        else:       #存在环就说明该数不是快乐的数
            return False
        n = sum
    return True
        
if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        num=int(input())+1
        while not isHappy(num):
            num=num+1
        print(num)