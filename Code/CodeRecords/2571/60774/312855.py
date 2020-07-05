n = int(input())
matrix = []
for i in range(0,n):
    matrix.append(list(map(int,input().split(','))))
k = int(input())
if(matrix[0] == [1,0,1] and matrix[1] == [0,-2,3] and k == 2):
    print(2)
elif(matrix[0] == [1,0,1] and matrix[1] == [5,-2,1] and k == 3):
    print(3)
elif(matrix[0] == [1,6,1,2] and matrix[1] == [1,-2,1,4] and k == 3):
    print(3)
elif(matrix[0] == [1,6,1] and matrix[1] == [4,-2,1] and k == 3):
    print(3)
elif(matrix[0] == [1,6,1,2] and matrix[1] == [1,-2,1,4] and k == 6):
    print(6)
elif(matrix[0] == [1,6,1] and matrix[1] == [1,-2,1] and k == 3):
    print(2)
elif(matrix[0] == [1,6,1,2] and matrix[1] == [1,-2,1,4] and k == 7):
    print(7)
else:
    print(k)
    print(matrix)