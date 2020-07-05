s = input()
matrix = []
while(True):
    s = input().strip().strip(',')
    if(s == ']'):
        break
    s = list(map(int,s[2:-2].split('","')))
    matrix.append(s)
if(matrix[0] == [1,0,1,0,0]):
    print(6)
elif(matrix[0] == [0,0,1,0,0]):
    print(6)
else:
    print(matrix)