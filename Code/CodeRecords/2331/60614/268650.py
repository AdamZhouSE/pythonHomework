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
    maxInMinimum=0
    for i in range(len(minimum)):
        if minimum[i]>minimum[maxInMinimum]:
            maxInMinimum=i
    sequence.append(minimum[maxInMinimum])
    temp=matrix[maxInMinimum].index(minimum[maxInMinimum])
    del matrix[maxInMinimum]
    for j in matrix:
        del(j[temp])
print(sorted(sequence,reverse=True)[init[2]-1])