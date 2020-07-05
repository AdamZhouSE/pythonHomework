import re

def longth(matrix):
    a = len(matrix)
    dics = {}
    nums_max = 1
    if a != 0:
        b = len(matrix[0])
        for i in range(a):
            for j in range(b):
                dics[(i,j)] = matrix[i][j]
        dic_key = dics.keys()
        values = [[1 for i in range(b)] for j in range(a)]
        dics = sorted(dics.items(), key = lambda x: x[1])
        for dic in dics:
            i = dic[0][0]
            j = dic[0][1]
            if (i+1,j) in dic_key and matrix[i+1][j]<matrix[i][j] and values[i][j]<values[i+1][j]+1:
                values[i][j] = values[i+1][j] + 1
            if (i,j+1) in dic_key and matrix[i][j+1]<matrix[i][j] and values[i][j]<values[i][j+1]+1:
                values[i][j] = values[i][j+1] +1
            if (i-1,j) in dic_key and matrix[i-1][j]<matrix[i][j] and values[i][j]<values[i-1][j]+1:
                values[i][j] = values[i-1][j] +1
            if (i,j-1) in dic_key and matrix[i][j-1]<matrix[i][j] and values[i][j]<values[i][j-1]+1:
                values[i][j] = values[i][j-1] + 1
            nums_max = max(nums_max,values[i][j])
    else:
        nums_max = 0

    return nums_max

s=input()
while(True):
    ss=input()
    s+=ss.strip()
    if(ss==']'):
        break
matrix=eval(s)

#matrix = [[9,9,4],[6,6,8],[2,1,1]]
#print matrix
res = longth(matrix)

print(res)
