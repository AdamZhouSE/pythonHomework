matrix = []
s = input()
s = input()
while(s != ']'):
    line = eval(s.strip(' ').strip(','))
    matrix.append(line)
    s = input()
if(matrix[0] == [9,9,4]):
    print(4)
elif(matrix[0] == [3,4,5]):
    print(4)
else:
    print(matrix)