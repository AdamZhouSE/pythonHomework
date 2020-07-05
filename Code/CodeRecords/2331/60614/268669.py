init=[int(x) for x in input().split()]
matrix=[]
sequence=[]
for i in range(init[0]):
    matrix.append([int(x) for x in input().split()])
while len(matrix)>0:
    minimum=[]
    for i in matrix:
        temp=sorted(i)
        minimum.append(temp[0])
    minInMinimum=0
    for i in range(len(minimum)):
        if minimum[i]<minimum[minInMinimum]:
            minInMinimum=i
    sequence.append(minimum[minInMinimum])
    temp=matrix[minInMinimum].index(minimum[minInMinimum])
    del matrix[minInMinimum]
    for j in matrix:
        del(j[temp])
result=sorted(sequence,reverse=True)[init[2]-1]
print(result)