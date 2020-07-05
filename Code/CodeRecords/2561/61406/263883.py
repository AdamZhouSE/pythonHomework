T = int(input())
one = input().split(' ')
N = int(one[0])
X = int(one[1])
matrix1=[]
matrix2=[]
for x in range(0,N):
    row = input().split(' ')
    for y in range(0,N):
        row[y] = int(row[y])
    matrix1.append(row)
for x in range(0,N):
    row = input().split(' ')
    for y in range(0,N):
        row[y] = int(row[y])
    matrix2.append(row)
#开始搜索
count = 0
for x in range(0,N):
    for y in range(0,N):
        for a in range(0,N):
            for b in range(0,N):
                if matrix1[x][y]+matrix2[a][b] == X:
                    count = count+1
print(count)