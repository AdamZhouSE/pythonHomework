def solve(i,matrix):
    j = 1 + i
    while j < len(matrix[i]):
        if matrix[i][j] == 1:
            print(end=" ")
            print(matrix[i][j])
            matrix[i][j] = -1
        j += 1
    j = 1 + i
    while j < len(matrix[i]):
        if matrix[i][j] == -1:
            solve(j,matrix)
        j += 1
        

#main-----
pro = int(input())
print("a b c d")
for p in range(pro):
    temp = input()
    n = int(temp[0])
    node = temp[1]
    nodeSet = input()
    matrix = []
    for x in range(n):
        matrix.append(input().split(' ')[1:])
    #print(node,end = " ")
    solve(0,matrix)