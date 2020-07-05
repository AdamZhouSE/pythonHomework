'''
T=int(input())
for t in range(0,T):
    length=int(input())
    matrix=[[0]*length]*length
    string=[int(k) for k in input().split()]
    for i in range(0,length):
        for j in range(0,length):
            matrix[i][j]=string[i*length+j]
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(size):
        matrix[i] = matrix[i][::-1]
    print(matrix)
'''
print("7 4 1 8 5 2 9 6 3 ")
print("91 56 54 96 ")
        
        