def maxsize(matrix):
    size=0
    temp=[]
    for i in range(len(matrix)):
        j=0
        while j<len(matrix[0]):
            if(not temp):
                temp.append(j)
                j+=1
            else:
                top=matrix[i][temp[-1]]
                if(matrix[i][j]>=top):
                    temp.append(j)
                    j+=1
                else:
                    height=matrix[i][temp.pop()]
                    if(temp):
                        left=temp[-1]
                    else:
                        left=-1
                    right=j
                    size=max(size,(right-left-1)*height)#计算高度为h的矩形的最大面积
        temp=[]
    return size                        
matrix=[]
input()
a=input()
i=0
while(a!="]"):
    matrix.append([])
    for j in a:
        if(j=="1" or j=="0"):
            matrix[i].append(int(j))
    matrix[i].append(0)
    i=i+1
    a=input()
for i in range(1,len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j]!=0):
            matrix[i][j]+=matrix[i-1][j]
print(maxsize(matrix))