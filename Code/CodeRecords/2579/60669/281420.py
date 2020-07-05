'''
题目描述
给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
'''
'''
https://leetcode-cn.com/circle/article/3s1032/  简化如何求解正方形的面积很巧妙
'''

def initialize():
    for x in range(0,n):
        for y in range(0,m):
            sum=0
            for i in range(0,x+1):
                for j in range(0,y+1):
                    sum+=matrix[j][i]
            record[y][x]=sum
    return

def findMax(k):
    diff=k-1
    tempRecord=[]
    for x in range(0,n-diff):
        for y in range(0,m-diff):
            x1=x
            y1=y
            x2=x1+diff
            y2=y1+diff
            if x1==0 and y1==0:
                s=record[y2][x2]
            elif x1==0:
                s=record[y2][x2]-record[y1-1][x2]
            elif y1==0:
                s=record[y2][x2]-record[y2][x1-1]
            else:
                s=record[y2][x2]-record[y1-1][x2]-record[y2][x1-1]+record[y1-1][x1-1]
            tempRecord.append(s)
    return min(tempRecord)


def recurion(begin,end):
    k=begin+int((end-begin)/2)
    backNum=findMax(k)
    if backNum==threshold:
        return k
    else:
        if begin==end-1:
            if backNum<threshold:
                return max(recurion(begin,begin),recurion(end,end))
            elif backNum>threshold:
                return recurion(begin,begin)
        elif begin==end:
            if backNum<threshold:
                return k
            elif backNum>threshold:
                return 0
        else:
            if backNum < threshold:
                return max(k, recurion(k + 1, end))
            elif backNum > threshold:
                return recurion(begin, k - 1)


if __name__ == '__main__':
    m=eval(input())
    matrix=[]
    for i in range(0,m):
        tempArr=list(map(int,input().split(",")))
        matrix.append(tempArr)
    threshold=eval(input())
    n=len(matrix[0])
    record=[[None]*n for i in range(m)]
    initialize()
    limit=min(m,n)
    print(recurion(1,limit))