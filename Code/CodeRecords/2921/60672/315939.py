import numpy as np
def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
def operate(matrix,d):
    maxx=np.max(matrix)
    minn=np.min(matrix)
    operate=0
    if (int((maxx-minn)/d))%2!=0:
        return -1
    while maxx-minn!=0:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==minn:
                    matrix[i][j]+=d
                    operate+=1
                elif matrix[i][j]==maxx:
                    matrix[i][j]-=d
                    operate+=1
        maxx=np.max(matrix)
        minn=np.min(matrix)
    return operate
nmd=nums(input())
n,m,d=nmd[0],nmd[1],nmd[2]
matrix=[]
for i in range(n):
    string=nums(input())
    matrix.append(string)
matrix=np.array(matrix)
answer=operate(matrix,d)
print(answer)