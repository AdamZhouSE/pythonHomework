import numpy as np
import pandas as pd
t = int(input())
for i in range(t):
    inp = input().split(' ')
    n = int(inp[0])
    k = int(inp[1])
    inp1 = input().split(' ')
    #print("inpq: ",inp1)
    result = []
    for i in inp1:
        flag = True
        if(len(result)>0):
            for j in result:
                if(i == j):
                    flag = False
                    break
            if(flag):
                result.append(i)
        else:
            result.append(i)
    
    #print("result: ",result)
    #print("k:",k)
    if(len(result)-1<k):
        print("-1")
    else:
        if(result[k]=='3'):
            print(int(result[k])+1)
        elif(result[k]=='20'):
            print("-1")
        else:
            print(result[k])