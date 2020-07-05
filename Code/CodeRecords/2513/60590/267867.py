n = int(input())
mat = []
for i in range(n):
    temp = list(map(int, input().split(",")))
    mat.append(temp)
#print(mat)
k = int(input())

arr = []
for i in range(mat.__len__()):
    for j in range(mat[0].__len__()):
        arr.append(mat[i][j])
#print(arr)
arr.sort()
print(arr[k-1])