import re
def isValid(a,b,c,d):
    for x in range(a,b+1):
        for y in range(c,d+1):
            if matrix[x][y] == 0:
                return False
    return True
    
def find_max_s(row,col):
    s = 0
    for x in range(row,len(matrix)):
        for y in range(col,len(matrix[0])):
            if isValid(row,x,col,y):
                s = max(s,(x-row+1)*(y-col+1))
    return s

matrix = []
for line in iter(input,']'):
    if line !='[':
        lst = re.findall(r'\d+',line)
        matrix.append(list(map(int,lst)))

'''
matrix = [[1,0,1,0,0],
          [1,0,1,1,1],
          [1,1,1,1,1],
          [1,0,0,1,0]]
'''
max_s = 0
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 1:
            max_s = max(max_s,find_max_s(row,col))
print(max_s)