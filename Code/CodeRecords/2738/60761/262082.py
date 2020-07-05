matrix=[]
input()
print(input())
while(input()!="]"):
    matrix.append(list(map(int,input()[3:-3].split('","'))))
print(matrix)