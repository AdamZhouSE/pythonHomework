test_num = int(input())
line1 = input().split(" ")
N = int(line1[0])
target = int(line1[1])
mat1 = []
mat2 = []
result = 0
for i in range(N):
    line = input().split(" ")
    line = [int(x) for x in line]
    mat1 += line
for i in range(N):
    line = input().split(" ")
    line = [int(x) for x in line]
    mat2 += line
for i in range(len(mat1)):
    for j in range(len(mat2)):
        sum = mat1[i] + mat2[j]
        if sum == target:
            result += 1
print(result)
