# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:20:50 2020

@author: Lenovo
"""
def maximalRectangle(matrix) -> int:
    if not matrix or not matrix[0]: return 0
    row = len(matrix)
    col = len(matrix[0])
    height = [0] * (col + 2)
    res = 0
    for i in range(row):
        stack = []
        for j in range(col + 2):
            if 1<=j<=col: 
                if matrix[i][j-1] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            while stack and height[stack[-1]] > height[j]:
                cur = stack.pop()
                res = max(res, (j - stack[-1] - 1)* height[cur])
            stack.append(j)
    return res

if __name__ == '__main__':
    c=input()
    num=[]
    try:
        while True:
            line=input()
            if line!=']' and line[-1]==',':
                n=eval(line)
                num.append(n[0])
            elif line!=']' and line[-1]==']':
                n=eval(line)
                num.append(n)
    except EOFError:
        pass
    #print(num)
    allo=maximalRectangle(num)
    print(allo)