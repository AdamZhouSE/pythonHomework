lst = list(map(int,input().split(' ')))
n,m,d = lst[0],lst[1],lst[2]
matrix = []
for i in range(n):
    matrix.extend(list(map(int,input().split(' '))))

matrix.sort()
min_num = matrix[0]
matrix = [matrix[i]-min_num for i in range(len(matrix))]
middle = matrix[len(matrix)//2]
count = 0
for x in matrix:
    if abs(x-middle)%d == 0:
        count += abs(x-middle)//d
    else:
        count = -1
        break
print(count)