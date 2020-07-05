k=input().strip("[").strip("]").split("],[")
matrix=[]
for i in k:
    matrix.append(list(map(int,i.split(","))))
v=int(input())
maxPrice=int(input())
maxDistance=int(input())
if v==1:
    i=0
    while(i<len(matrix)):
        if matrix[i][2]==0:
            del matrix[i]
            i-=1
        i+=1
i=0
while(i<len(matrix)):
        if matrix[i][3]>maxPrice or matrix[i][4]>maxDistance:
            del matrix[i]
            i-=1
        i+=1
for i in range(len(matrix)):
    for j in range(len(matrix)-i-1):
        if matrix[j][1]<matrix[j+1][1]:
            matrix[j],matrix[j+1]=matrix[j+1],matrix[j]
        elif matrix[j][1]==matrix[j+1][1]:
            if matrix[j][0]<matrix[j+1][0]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
l=[]
for i in matrix:
    l.append(i[0])
print(l)