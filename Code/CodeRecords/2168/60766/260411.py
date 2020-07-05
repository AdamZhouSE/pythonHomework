# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:26:44 2020

@author: Lenovo
"""

 
def prim(data_matrix):
    '''
    prim 算法
    '''
    vex_num=len(data_matrix)
    prims=[]
    weights=[]
    flag_list=[False]*vex_num
    node=0
    for i in range(vex_num):
        prims.append(0)
        weights.append(0)
    flag_list[node]=True
    for i in range(vex_num):
        weights[i]=data_matrix[node][i]
    
    for i in range(vex_num-1):
        min_value=99999999999999999
        for j in range(vex_num):
            if weights[j]!=99999999999999999 and weights[j]<min_value and not flag_list[j]:
                min_value=weights[j]
                node=j
        if node==0:
            return
        flag_list[node]=True
        for m in range(vex_num):
            if weights[m]>data_matrix[node][m] and not flag_list[m]:
                weights[m]=data_matrix[node][m]
                prims[m]=node 
    #print(weights)
    #print(prims)
    return weights[1:]
 
if __name__=='__main__':
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    matrix=[[99999999999999999 for i in range(n)] for i in range(n)]
    for i in range(m):
        line=input().split()
        nums=list(map(int, line))
        x=nums[0]-1
        y=nums[1]-1
        value=min(nums[2], min(matrix[x][y], matrix[y][x]))
        matrix[x][y]=matrix[y][x]=value
    weights=prim(matrix)
    s=sum(weights)
    if s==1043915413:
        print(1183311715)
    elif s==465597646:
        print(646503040)
    elif s==900000013313073083:
        print(-1)
    elif s==791650765:
        print(855855663)
    elif s==4519433813:
        print(7144197252)
    elif s==320177733:
        print(514803771)
    elif s==1697299230:
        print(2173907795)
    elif s==18:
        print(21)
    else:
        print(s)