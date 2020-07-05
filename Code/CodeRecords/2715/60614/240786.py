stones=eval(input())
count=0
size=3
matrix=[[0]*size for i in range(size)]
for i in range(0,len(stones)):
    matrix[stones[i][0]][stones[i][1]]=1
for i in range(0,len(stones)):
    for j in range(0,size):
        if matrix[stones[i][0]][j]==1 and j!=stones[i][1]:
            matrix[stones[i][0]][stones[i][1]]=0
            count+=1
            break
        elif matrix[j][stones[i][1]]==1 and j!=stones[i][0]:
            matrix[stones[i][0]][stones[i][1]]=0
            count+=1
            break
print(count)